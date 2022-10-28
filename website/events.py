from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment
from .forms import EventsForm, CommentForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('destination', __name__, url_prefix='/destinations')

<<<<<<< HEAD
#def book(): Ben sucks cock
=======
@bp.route
def book():
>>>>>>> bbf73c1161dbac513bf486978879d2d2cd905e6e
