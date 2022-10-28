from unicodedata import name
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment
from .forms import BookForm, EventsForm, CommentForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/book', methods = ['GET', 'POST'])
def book():
    form = BookForm()
    if form.validate_on_submit():
        event=Events(name=form.name.data,email=form.email_id.data, 
        phone=form.phone_number.data,ticet=form.ticket_amount.data)()
        db.session.add(event)
        db.session.commit
        print('Successfully booked event', 'success')
    return render_template('destinations/event details.html', form=form) 

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventsForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    event=Events(name=form.music_name.data, description=form.music_type.data,  
    image=db_file_path,name=form.artist_name.data,name=form.venue.data,description=form.event_status.data,description=form.enter_description.data)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('destinations.event creation'))
  return render_template('destinations/event creations.html', form=form)
