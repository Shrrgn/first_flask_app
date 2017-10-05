from flask.ext.wtf import  Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired,Length,EqualTo

#class LoginForm(Form):
	#openid = StringField('openid',validators=[DataRequired()])
	#remember_me = BooleanField('remember_me',default=False)

class LoginForm(Form):
	login = StringField('Login',validators=[DataRequired()])
	password = StringField('Password',validators=[DataRequired()])

class RegistrationForm(Form):
	login = StringField('Login:',validators=[DataRequired(),
											Length(min=5,max=12)])
	full_name = StringField('Full name:')
	hobby = StringField('Hobby:')
	password = PasswordField('Password:',validators=[DataRequired(),
				EqualTo('confirm',message='Password must match'),
				Length(min=8,max=25)])
	confirm = PasswordField('Repeat password:')

