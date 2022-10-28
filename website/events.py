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
        phone=form.phone_number,ticket=form.ticket_amount.data)()
        db.session.add(event)
        db.session.commit()
        print('Successfully created new travel destination', 'success')
    return render_template('events/book.html', form=form)