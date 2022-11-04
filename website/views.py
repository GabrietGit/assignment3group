from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events
from .forms import EventsForm
from . import db
from flask_login import login_required
import os
from werkzeug.utils import secure_filename

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    events = Events.query.all()    
    return render_template('index.html', events=events)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        evnt = "%" + request.args['search'] + '%'
        events = Events.query.filter(Events.description.like(evnt)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))

@mainbp.route('/event_creation')
def event_creation():
    return render_template('destinations/event_creation.html')

@mainbp.route('/event details/<id>')
def event_details(id):
    event_details = Events.query.filter_by(id=id).first()
    return render_template('destinations/event details.html', event_details=event_details)

@mainbp.route('/user')
def user():
    return render_template('destinations/user.html')

@mainbp.route('/booking_history')
def booking_history():
    return render_template('destinations/user booking history.html')

@mainbp.route('/create', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  FlaskForm = EventsForm()
  if FlaskForm.validate_on_submit():
    #gets details
    db_file_path=check_upload_file(FlaskForm)
    events=Events(music_name=FlaskForm.music_name.data,music_type=FlaskForm.music_type.data, 
    image=db_file_path,artist_name=FlaskForm.artist_name.data,date_and_time=FlaskForm.date_and_time.data,venue=FlaskForm.venue.data,event_status=FlaskForm.event_status.data,ticket_amount=FlaskForm.ticket_amount.data,description=FlaskForm.enter_description.data)
    # add the object to the db session
    db.session.add(events)
    # commit to the database
    db.session.commit()
    print('Successfully created new music event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('destination.event_creation'))
  return render_template('destinations/event_creation.html', FlaskForm=FlaskForm)

def check_upload_file(FlaskForm):
  #get file data from form  
  fp=FlaskForm.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path