from flask_app import app
from flask import render_template
from flask_app.getProjects import getProjects
from flask import jsonify, send_from_directory
import os

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'templates')

@app.route('/')
def index():
   # return "Hello World!"
   return render_template('index.html')

@app.route('/projects')
def projects():
	return jsonify(getProjects())

# @app.route('/picture')
# def image():
#    return render_template('index.html')