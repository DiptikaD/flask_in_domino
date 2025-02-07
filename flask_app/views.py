from flask_app import app
from flask_app.getProjects import getProjects
from flask import jsonify, send_from_directory
import os

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/')
def index():
   return "Hello World!"

@app.route('/projects')
def projects():
	return jsonify(getProjects())

@app.route('/picture')
def image():
   return send_from_directory(STATIC_FOLDER, 'sheep_pose.jpg')