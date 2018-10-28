from app import database as db


class KnowledgeBase(db.Model):
	"""
	This is the database of where some fun activities for kids would be stored
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(150), nullable = False)
	describe = db.Column(db.String(1000), nullable=False)
	
	db.create_all()
	def addKnowledgeBase(param_title, param_describe):
		kb = KnowledgeBase( title = param_title,describe= param_describe)
		db.session.add(kb)
		db.session.commit()
		return True

	def getKnowledgeBaseInfo(knowledgebase_id):
		return db.session.query(KnowledgeBase).get(knowledgebase_id)

	def deleteKnowledge(knowledgebase_id):
		KnowledgeBase.query.filter_by(id=knowledgebase_id).delete()
		print("Deleted Knowledge Base with id " + str(knowledgebase_id))

	





