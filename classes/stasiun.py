from utils import model as DbModel

class Stasiun:
	def get_all():
		db = DbModel.DbModel()
		db.connect()
		query = "SELECT * FROM stasiun"
		db.cursor.execute(query)
		rows = db.cursor.fetchall()
		result = [dict(row) for row in rows] if rows else None
		db.close()
		return result