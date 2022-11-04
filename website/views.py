from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events
from .forms import EventsForm, Form
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

@mainbp.route('/event details')
def event_details():
    return render_template('destinations/event details.html')

@mainbp.route('/user')
def user():
    return render_template('destinations/user.html')

@mainbp.route('/create', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = EventsForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    events=Events(name=form.name.data,description=form.description.data, 
    image=db_file_path,currency=form.currency.data)
    # add the object to the db session
    db.session.add(events)
    # commit to the database
    db.session.commit()
    print('Successfully created new travel destination', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('events.create'))
  return render_template('destinations/event_creation.html', form=form)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
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