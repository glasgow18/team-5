from app import database as db

class Badges(db.Model):
	"""
	This Database was made for Badges (Achievements) the user could possibly achieve
	"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True) #Unique Indentifier automatically keeps itself unique on addition
	badgeName = db.Column(db.String(150), nullable = False)
	description = db.Column(db.String(1150), nullable=False)

	db.create_all()
	"""
	Add a badge by its name and its description of what it is, could possibly have more paramaters for a badge
	"""
	def addBadges(param_badgeName, param_description):
		badges = Badges(badgeName = param_badgeName, description = param_description)

		db.session.add(badges)
		db.session.commit()
		return True
	"""
	Return badge by unique badge id
	"""
	def getBadge(badge_id): #Uses unique identifier to retrieve badge
		return db.session.query(Badges).get(badge_id)
	



print(Badges.addBadges("badge","a new badge"))
print(Badges.getBadge(1))
