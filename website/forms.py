
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
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

class EventsForm(FlaskForm):
  Music_name = StringField('Music Name', validators=[InputRequired()])
  Music_type = TextAreaField('Music Type', 
            validators=[InputRequired()])
  image = FileField('Upload Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  Artist_Name = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")

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
