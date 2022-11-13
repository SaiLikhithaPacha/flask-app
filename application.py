from flask import Flask
application = Flask(__name__)

@application.route('/')

def hello_world():
	return 'Heyy, Welcome to the page where we deployed using Beanstalk!'
