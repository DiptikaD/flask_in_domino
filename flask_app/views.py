from flask_app import app
from flask_app.getProjects import getProjects
from flask import jsonify
from flask import Flask

	# hardcoding the project id as the static url
app = Flask(__name__, static_url_path='/modelproducts/67a52df95b902c4c38746378')

#@app.route('/')
#def index():
#    return "Hello World!"

@app.route('/')
def projects():
	return jsonify(getProjects())