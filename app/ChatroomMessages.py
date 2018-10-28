from datetime import datetime
from app import database as db

class ChatroomMessages(db.Model):
	"""
	This database is for storing the actual messages in a chatroom, and connects to a chatroom using the chatroom ID
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	chatroomID = db.Column(db.Integer)
	message = db.Column(db.String(10050), nullable = False)
	sentUserID = db.Column(db.Integer, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False)

	db.create_all()
	"""
	Add a new message to a chatroom
 	"""
	def addChatroomMessage(param_chatroomID, param_message, param_sentuserID, param_timestamp):
		chatroom_message = ChatroomMessages(chatroomID = param_chatroomID, message = param_message, sentUserID = param_sentUserID, timestamp = param_timestamp)
		db.session.add(chatroom_message)
		db.session.commit()
		return True #Confirmation that it added the chatroom successfully
	"""
	Retrieve messages by unique chatroom ID
	"""
	def getChatroomMessages(param_chatroom_id):
		return ChatroomMessages.query.filter_by(chatroomID=param_chatroom_id)


