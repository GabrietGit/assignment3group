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
    print('Method type: ', request.method)
    form = BookForm()
    if form.validate_on_submit():
         db_file_path=check_upload_file(form)
         event=Events(name=form.name.data,description=form.description.data, 
    image=db_file_path,currency=form.currency.data)()