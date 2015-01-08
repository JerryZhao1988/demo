# before running this app, must do "export FLASKR_SETTINGS=~/path/settings.py" first

import flask
import settings
import os

from flask import g
from index import Index
from flask import session
from database import Database

app = flask.Flask(__name__)

# export FLASKR_SETTINGS=/settings.py
app.config.from_envvar('FLASKR_SETTINGS', silent=False)

DA = Database(app.config['DATABASE'])


@app.before_request
def before_request():
	g.db = DA.connect_db()


@app.route('/add_entry',methods=['POST'])
def add_entry():
	if DA.add(flask.request.form['pic']):
		return "New liked Img was successfully added"
	else:
		return "This img is liked before"

@app.route('/show_liked', methods=['POST','GET'])
def show_liked():
	session["result"]=DA.show()
	return flask.render_template('show.html')

@app.route('/delete_img', methods=['POST'])
def delete_img():
	if DA.delete(flask.request.form['pic']):
		return "Image has deleted from liked Img"

# @app.cli.command('init_db')
# def initdb_command():
# 	DA.initdb()

@app.teardown_appcontext
def close_db(error):
	DA.close(error)

app.add_url_rule('/', view_func=Index.as_view('index'), methods = ["GET" ,"POST"])
app.run(host='0.0.0.0')
