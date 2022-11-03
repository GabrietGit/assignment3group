from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events

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
    return render_template('event_creation.html')