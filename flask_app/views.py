from flask_app import app
from flask_app.getProjects import getProjects
from flask import jsonify

@app.route('/')
def index():
   return "Hello World!"

@app.route('/projects')
def projects():
	return jsonify(getProjects())