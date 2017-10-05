
from flask_login import UserMixin, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

	def __init__(self, login=None, password=None):
		self._login = login
		self._password = generate_password_hash(password)
		self._hobby = None
		self._full_name = None

	@property
	def login(self):
		return self._login
	
	@property
	def password(self):
		return self._password

	@property
	def hobby(self):
		return self._hobby
	
	@property
	def full_name(self):
		return self._full_name
		
	@login.setter
	def login(self,value):
		self._login = value	

	@password.setter
	def password(self,value):
		self._password = generate_password_hash(value)	

	@hobby.setter
	def hobby(self,value):
		self._hobby = value	

	@full_name.setter
	def full_name(self,value):
		self._full_name = value	

	def verify_password(self,pswd):
		return check_password_hash(self._password,pswd)

	def __repr__(self):
		return 'User login {}, password {}'.format(self._login,self._password)

	def is_activate(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	def get_id(self):
		return self.login