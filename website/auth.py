from flask import Blueprint, flash, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db


#create a blueprint
bp = Blueprint('auth', __name__)



@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True ):
        username = register.user_name.data
        pwd = register.password.data
        email = register.email_id.data
        #Check if user exists
        u1 = User.query.filter_by(name = username).first()
        if u1:
            flash("Username already exists, please login")
            return redirect(url_for('auth.login'))
        pwd_hash = generate_password_hash(pwd)
        new_user = User(name = username, password_hash = pwd_hash, emailid = email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form = register, heading = 'Register')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name = user_name).first()
        if u1 is None:
            error = 'Incorrect User name'
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form = login_form, heading = 'Login')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You have been logged out'
     