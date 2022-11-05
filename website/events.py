from asyncio import events
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment
from .forms import BookForm, EventsForm, CommentForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = Events.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('events/event details.html', event=event, form=cform)

@bp.route('/event details')
def event_creation():
    return render_template('events/event details.html')

@bp.route('/book', methods = ['GET', 'POST'])
def book():
    print('Method type: ', request.method)
    form = BookForm()
    if form.validate_on_submit():
        event=Events(name=form.name.data,email=form.email_id.data, 
        phone=form.phone_number.data,ticket=form.ticket_amount.data)()
        db.session.add(event)
        db.session.commit
        print('Successfully booked event', 'success')
    return render_template('events/event details.html', form=form)
    


  