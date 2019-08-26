import os
import sys
from flask import Flask, url_for, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////'+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dev'

db =SQLAlchemy(app)

class Survey(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	client = db.Column(db.String(200), unique=True)
	employee = db.Column(db.String(200))
	rating = db.Column(db.Integer)
	comments=db.Column(db.Text())

@app.route('/', methods=['GET','POST'])
def index():
	if request.method=='POST':
		client = request.form.get('client')
		employee = request.form.get('employee')
		rating = request.form.get('rating')
		comments=request.form.get('comments')
		if not client or not employee or not rating or not comments:
			flash('Invalid Input')
			return redirect(url_for('index'))
		survey = Survey(client=client, employee=employee, rating=rating, comments=comments)
		db.session.add(survey)
		db.session.commit()
		flash('Survey Submitted')
		send_email(client,employee,rating,comments)
		return redirect(url_for('submission'))
	return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'),404
