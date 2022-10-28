from multiprocessing import Event
from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/')
def index():
    events = Events.query.all()    
    return render_template('index.html', events=events)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        evnt = "%" + request.args['search'] + '%'
        events = Events.query.filter(Event.description.like(evnt)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))