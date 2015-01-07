import flask, flask.views
from sax import Test
from flask import session
import re


class Index(flask.views.MethodView):
	def get(self):
		session.clear()	
		result = Test('')
		session["result"] = result
		return flask.render_template('base.html')

	def post(self):
		query = str(flask.request.form['expression'])
		if self.filter(query):
			return flask.render_template('base.html')
		result = Test(query)

		if len(result) == 0:
			flask.flash("No result!~")
		else:
			session["result"] = result
		
		return flask.render_template('base.html')

	def filter(self,expression):
		p=re.compile(r'["\']')	
		if expression == "": 
			flask.flash("input should not be empty!~")
			return True
		elif p.search(expression):
			flask.flash("invalid input!~")
			return True
		return False
