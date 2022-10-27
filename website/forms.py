
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#books event
class BookForm(FlaskForm):
  name = StringField('Event', validators=[InputRequired()])
  email_id = StringField('Email Address', validators=[Email('Please enter a valid email')])
  phone_number = StringField('Phone Number', validators=[InputRequired()])
  ticket_amount = StringField('Ticket Amount', validators=[InputRequired()])
  submit = SubmitField("Book")

#Events Creation
class EventsForm(FlaskForm):
  music_name = StringField('Music Name', validators=[InputRequired()])
  music_type = SelectField(u'Music Type', 
            choices=[('None'), ('Classical'), ('Pop'), ('Jazz'), ('Rock'), ('Country')])
  image = FileField('Upload Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  artist_name = StringField('Artist Name', format='%Y-%m-%d'())
  date_and_time = DateField('Date and Time', validators=[InputRequired()])
  venue = StringField('Venue', validators=[InputRequired()])
  event_status = StringField('Event Status', validators=[InputRequired()])
  enter_description = StringField('Enter a description for the event', validators=[InputRequired()])
  submit = SubmitField("Confirm")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")
