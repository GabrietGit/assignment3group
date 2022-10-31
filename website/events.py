
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

>>>>>>> 16cebb4ff286e4e4a6ca1d41c8cf5ef87ba1e1c7
@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventsForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    destination=Events(name=form.name.data,description=form.description.data, 
    image=db_file_path,currency=form.currency.data)
    # add the object to the db session
    db.session.add(destination)
    # commit to the database
    db.session.commit()
    print('Successfully created new travel destination', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('events.create'))
  return render_template('events/user booking history.html', form=form)

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