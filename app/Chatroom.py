from datetime import datetime
from app import database as db

class Chatroom(db.Model):
	"""
	This database keeps track of creation date of a Chatroom, the date the chatroom was last updated, a type , and a nice colour to be welcoming!
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) #Unique Identifier to auto increment
	name = db.Column(db.String(150), nullable = False)
	creationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	lastUpdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	colour = db.Column(db.String(150), nullable=False)
	chattype = db.Column(db.String(150), nullable=False) #The moderator who creates the chatroom can choose b/w different types, or add a new one

	db.create_all()

	
	def addNewChatroom(param_name, param_creationDate, param_lastUpdate, param_colour, param_chattype):
		chat = Chatroom(name = param_name, creationDate = param_creationDate, lastUpdate = param_lastUpdate, colour = param_colour, chattype = param_chattype )
		db.session.add(chat)
		db.session.commit()
		return True
    
	"""
	Returns all the current types of chatrooms. Can be used by moderator to make a chatroom of an already existing type
	"""
	def getAllTypes(): #So the creator of the Chatroom can select from already available types
		return set(chatroom.chattype for chatroom in Chatroom.query.all())
    
	def getChatroomById(chatroom_id):
		return db.session.query(Chatroom).get(chatroom_id)
	
	def deleteById(chatroom_id):
		Chatroom.query.filter_by(id=chatroom_id).delete()
		print("Deleted Chatroom with id " + str(chatroom_id))



