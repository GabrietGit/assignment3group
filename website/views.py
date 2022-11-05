from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events, Bookings
from .forms import EventsForm, BookForm, CommentForm
from . import db
from flask_login import login_required
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateField, FloatField, FileField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, url, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed
from flask_wtf import FlaskForm as FlaskFormWTF

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

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
    FlaskForm = CommentForm()
    return render_template('destinations/event details.html', FlaskForm=FlaskForm, event_details=event_details)

@mainbp.route('/user')
def user():
    return render_template('destinations/user.html')

@mainbp.route('/booking_history')
def booking_history():
    return render_template('user booking history.html')

@mainbp.route('/edit/<id>', methods = ['GET', 'POST'])
def select_edit(id):
    select_edit = Events.query.filter_by(id=id).first()
    FlaskForm = EventsForm()
    if FlaskForm.validate_on_submit():
          select_edit.music_name = FlaskForm.music_name.data
          select_edit.music_type = FlaskForm.music_type.data
          select_edit.artist_name = FlaskForm.artist_name.data
          select_edit.date_and_time = FlaskForm.date_and_time.data
          select_edit.venue = FlaskForm.venue.data
          select_edit.event_status = FlaskForm.event_status.data
          select_edit.ticket_amount = FlaskForm.ticket_amount.data
          select_edit.description = FlaskForm.enter_description.data
          db.session.commit()                 
          return redirect(url_for('main.index'))
    return render_template('destinations/event_creation.html', FlaskForm=FlaskForm, select_edit=select_edit)

@mainbp.route('/base/<searchCategories>')
def category_base(searchCategories):
    if searchCategories == 'Classical':
        events = Events.query.filter_by(music_type=searchCategories).all()
        return render_template('index.html', events=events)
    elif searchCategories == 'Pop':
        events = Events.query.filter_by(music_type=searchCategories).all()
        return render_template('index.html', events=events)
    elif searchCategories == 'Jazz':
        events = Events.query.filter_by(music_type=searchCategories).all()
        return render_template('index.html', events=events)
    elif searchCategories == 'Rock':
        events = Events.query.filter_by(music_type=searchCategories).all()
        return render_template('index.html', events=events)
    elif searchCategories == 'Country':
        events = Events.query.filter_by(music_type=searchCategories).all()
        return render_template('index.html', events=events)
    else: events = Events.query.filter_by(music_type=searchCategories).all()

    return render_template('index.html', events=events)

@mainbp.route('/create', methods = ['GET', 'POST'])
@login_required
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
    return redirect(url_for('main.index'))
  return render_template('destinations/event_creation.html', FlaskForm=FlaskForm)

def book():
    print('Method type: ', request.method)
    FlaskForm = BookForm()
    if FlaskForm.validate_on_submit():
        booking=Bookings(name=FlaskForm.full_name.data,email=FlaskForm.email_address.data,
        phone=FlaskForm.phone_number.data,ticket=FlaskForm.enter_ticket_amount.data)()
        db.session.add(booking)
        db.session.commit
        print('Successfully booked event', 'success')
        return redirect(url_for('main.index'))
    return render_template('destinations/event details.html', FlaskForm=FlaskForm)

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