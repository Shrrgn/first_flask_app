from flask import render_template,flash,redirect,g,url_for
from app import app
from .forms import LoginForm,RegistrationForm #get object from forms.py
from .models import User
from .repo import UserRepo
from flask_login import LoginManager,login_user,logout_user,current_user,login_required

login_manager = LoginManager()
#login_manager.session_protection()
login_manager.init_app(app)

"""
@app.before_request
def before_request():
	g.user = current_user
"""

@login_manager.user_loader
def load_user(nickname):
	return UserRepo().get_user_by_name(nickname)

@app.route('/')
@app.route('/index_demo/')
#@login_required
def index():
	return render_template('index_demo.html',
							title='Home',
							page_name='Index Page')

@app.route('/welcome_demo/')
@login_required
def welcome_demo():
	return render_template('welcome_demo.html',
							title='Welcome',
							page_name='Welcome')

@app.route('/profile_demo/')
@login_required
def profile_demo():
	return render_template('profile_demo.html',
							title='Profile',
							page_name='Profile')





@app.route('/login_demo/',methods = ['POST','GET'])
def login_demo():
	form = LoginForm()
	if form.validate_on_submit():
		u = User(form.login.data,form.password.data)
		k = UserRepo().get_user_by_name(form.login.data)
		if k:
			login_user(k)
			flash('Login requested for login = "%s"' %(form.login.data))
			return redirect('/welcome_demo')
	return render_template('login_demo.html',
				title='Sign In Demo',
				page_name='Sign In',
				form=form)


@app.route('/registration_demo/',methods = ['GET','POST'])
#@login_manager.user_loader
def registration_demo():
	form = RegistrationForm()
	
	if  form.validate_on_submit():
		
		u = User(form.login.data,form.password.data)
		u.hobby = form.hobby.data
		u.full_name = form.full_name.data
		UserRepo().save(u)
		login_user(u)
		flash('Thanks for registration')
		return redirect('/welcome_demo')
	
	return render_template('registration_demo.html',
				title='Registration',
				page_name='Registration',
				form=form)


@app.route('/logout/')
@login_required
def logout():
	#user = current_user
	#user.authenticated = False
	logout_user()
	flash("You've been logged out" )
	return redirect('/index_demo')
