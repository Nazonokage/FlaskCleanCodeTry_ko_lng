# auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from app.models import User, Log
from app.forms import RegistrationForm, LoginForm
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            print("[DEBUG] Form validation passed")
            
            # Create user with SHA-256 hashing
            user = User(
                username=form.username.data,
                email=form.email.data
            )
            user.set_password(form.password.data)  # Use SHA-256 hashing
            
            print(f"[DEBUG] User created: {user.__dict__}")
            
            db.session.add(user)
            db.session.commit()
            print("[DEBUG] User committed to database")
            
            # Create log entry
            log = Log(
                ip_address=request.remote_addr,
                browser=request.headers.get('User-Agent'),
                path=request.path,
                timestamp=datetime.now(),
                user_id=user.id
            )
            db.session.add(log)
            db.session.commit()
            print("[DEBUG] Log entry committed")
            
            flash('Registration successful!', 'success')
            return redirect(url_for('auth.login'))

        except Exception as e:
            db.session.rollback()
            print(f"[ERROR] Database error: {str(e)}")
            flash(f'Database error: {str(e)}', 'error')
    
    elif request.method == 'POST':
        print("[DEBUG] Form validation failed:", form.errors)
        
    return render_template('register.html', form=form)

# auth.py
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):  # Use SHA-256 verification
            session['user_id'] = user.id
            session['logged_in'] = True
            session['username'] = user.username  # Store username in session
            
            # Log the login
            log = Log(
                ip_address=request.remote_addr,
                browser=request.headers.get('User-Agent'),
                path=request.path,
                timestamp=datetime.now(),
                user_id=user.id
            )
            db.session.add(log)
            db.session.commit()
            
            flash('Login successful!', 'success')
            return redirect(url_for('routes.dashboard'))
        flash('Invalid credentials', 'error')
    return render_template('login.html', form=form)


# auth.py
@auth_bp.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))