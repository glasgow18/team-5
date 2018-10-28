from datetime import datetime
from app import database as db

class Profile(db.Model):
	"""
	A basic database to store users details, unique identifier being their id, uniqueness in email is handled by web backend
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(150), nullable = False)
	level = db.Column(db.String(150), nullable=False)
	username = db.Column(db.String(150), nullable=False)
	colour = db.Column(db.String(150), nullable=False)
	date_of_birth = db.Column(db.DateTime,nullable=False)
	password = db.Column(db.String(150), nullable=False) #Stored in plaintext for now
	chatroomID = db.Column(db.Integer, nullable = False)

	db.create_all()

	"""
	Dummy Implementations for methods we would have implemented realistically if given the time
	"""
	@property
	def is_active(self): 
		return True

	"""
	Dummy Implementations for methods we would have implemented realistically if given the time
	"""
	@property
	def is_authenticated(self):
		return True

	"""
	Dummy Implementations for methods we would have implemented realistically if given the time
	"""
	@property
	def is_anonymous(self): 
		return False

	"""
	Dummy Implementations for methods we would have implemented realistically if given the time
	"""
	def get_id(self):
		return self.session_token


	def addProfile(param_email, param_level,pusername ,param_colour,param_date_of_birth, param_password, param_chatroomID):
		profile = Profile(email = param_email, level = param_level,username = param_username, colour = param_colour,date_of_birth = param_date_of_birth, password = param_password, chatroomID = param_chatroomID)
		db.session.add(profile)
		db.session.commit()
		return True
    	"""
	Email is unique (handled by web backend), thus can be used to query for user uniquely
	"""
	def getUserWithEmail(email):
		return Profile.query.filter_by(email=email).first()
	"""
	Retrieve users with the unique user id
	"""
	def getUserDetails(uid):
		return db.session.query(Profile).get(uid)

	"""
	Delete user using user id
	"""
	def deleteUserDetails(uid):
		Profile.query.filter_by(id=uid).delete()
		print("Deleted Profile with id " + str(uid))

	"""
	Very basic authorization method, no real security 
	"""
	@staticmethod
	def auth(uid, key):
		first_var = Profile.query.filter_by(id=uid).first()
		if ( (first_var.id == uid) &  (first_var.password == key)):
			return True
		return False
	
