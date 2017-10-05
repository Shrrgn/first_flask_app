
from psycopg2 import connect, paramstyle
from .models import User

class UserRepo:
	"""docstring for UserRepo __init__(self, arg):
		super(UserRepo__init__()
		self.arg = arg
	"""
	def __init__(self):
		self._conn = connect(database="users",user="hoholyuk",password="password",host="127.0.0.1")
		if not self._conn:
			raise Exception

	def save(self,user):
		sql = """insert into users (login,full_name,hobby,password) 
			  	 values (%(login)s,%(full_name)s,%(hobby)s,%(password)s)"""
		c = self._conn.cursor()
		c.execute(sql, {'login':user.login,'full_name':user.full_name,
						'hobby':user.hobby,'password':user.password})
		self._conn.commit()
		c.close()
	
	def get_user_by_name(self,login):
		sql = """select * from users where login=%(login)s """
		c = self._conn.cursor()
		c.execute(sql,{'login':login})
		row = c.fetchone()
		u = User(row[1],row[4])
		u.full_name = row[2]
		u.hobby = row[3]
		return u
		
	def get_user_by_login_password(self,login,password):
		sql = """select * from users where login=%(login)s 
				and password=%(password)s"""
		c = self._conn.cursor()
		c.execute(sql,{'login':login,'password':password})
		row = c.fetchone()
		u = User(row[1],row[4])
		u.full_name = row[2]
		u.hobby = row[3]
		return u