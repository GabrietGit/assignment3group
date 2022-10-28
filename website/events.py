from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment
from .forms import EventsForm, CommentForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user


#def book(): Ben sucks cock