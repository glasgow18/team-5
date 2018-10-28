from datetime import datetime
from app import database as db


class Messages(db.Model):
	"""
	This will store the plaintext messages - could be stored encrypted, This one is specific to messages b/w two people
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	message = db.Column(db.String(10050), nullable = False)
	sentUserID = db.Column(db.Integer, nullable=False)  #Identify sender
	receivedUserID = db.Column(db.Integer, nullable=False) # and receiver by their user IDs
	timestamp = db.Column(db.DateTime, nullable=False)

	db.create_all()
	def addMessage(param_message, param_sentUserID, param_receivedUserID, param_timestamp):
		message = Messages(message = param_message, sentUserID = param_sentUserID, receivedUserID = param_receivedUserID, timestamp = param_timestamp)
		db.session.add(message)
		db.session.commit()
		return True
	def getAllSentMessages(uid):
		return Messages.query.filter_by(sentUserID=uid).all()
	def getAllReceivedMessages(uid):
		return Messages.query.filter_by(receivedUserID=uid).all()
