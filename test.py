import unittest

from app import app, db, Survey

class SurveyTestCase(unittest.TestCase):
	def setUp(self):
		app.config.update(
			TESTING=True,
			SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
		)
		id = db.Column(db.Integer, primary_key=True)

		db.create_all()
		survey=Survey(customer="Customer", employee="Employee",rating=9, comments="Good")
		db.session.add_all([survey])
		db.session.commit()

		self.client=app.test_client()
		self.runner=app.test_cli_runner()

	def removeServer(self):
		db.session.remove()
		db.drop_all()

	def test_exist(self):
		self.assertIsNotNone(app)

	def test_404(self):
		res =self.client.get('/errorrrrr')
		self.assertEqual(res.status_code, 404)

	def test_index(self):
		res =self.client.get('/')
		self.assertEqual(res.status_code, 200)

	if __name__ =='__main__':
		unittest.main()

