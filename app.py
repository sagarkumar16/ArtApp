from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(200), nullable = False)
	description = db.Column(db.String(1000), nullable = True)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return "Hola!!"
	else: 
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)
