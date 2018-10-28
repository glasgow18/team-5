from datetime import datetime
from app import database as db

class Friends(db.Model):
	"""
	This represents the relationship between two friends using their unique User IDs
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	friend1UserID = db.Column(db.Integer)
	friend2UserID = db.Column(db.Integer)

	db.create_all()
	"""
	Store a pair of friends
	"""
	def addFriends(param_friend1UserID, param_friend2UserID):
		friends = Friends(friend1UserID = param_friend1UserID, friend2UserID = param_friend2UserID)
		db.session.add(friends)
		db.session.commit()
		return True
	"""
	For a user, it checks the relationship both ways, as friendship goes both ways :)
	"""
	def getUsersFriends(param_userID):
		friendsList = []
		friendsList.append(Friends.query.filter_by(friend1UserID = param_userID).first().friend2UserID)
		friendsList.append(Friends.query.filter_by(friend2UserID = param_userID).first().friend1UserID)
		return friendsList





