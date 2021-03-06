from baseDAO import BaseDAO
from contextlib import closing
from flask import g
import flask
import os
import sqlite3
from sqlite3 import dbapi2 as sqlite3

class DbDAO(BaseDAO):
	def __init__(self,path):
		super(self.__class__,self).__init__()
		self.path = path

	def setup(self):
		rv = sqlite3.connect(self.path)
		rv.row_factory = sqlite3.Row
		return rv

	def init_db(self):
		db = self.get_db()
		with app.open_resource('schema.sql', mode= 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()	

	def initdb(self):
		self.init_db()
		print('Initialized the database')

	def get_db(self):
	    """Opens a new database connection if there is none yet for the
	    current application context.
	    """
	    if not hasattr(g, 'sqlite_db'):
	        g.sqlite_db = self.setup()
	    return g.sqlite_db

	def teardown(self,error):
		"""Closes the database again at the end of the request."""
		if hasattr(g, 'sqlite_db'):
			g.sqlite_db.close()
		

	def add(self,url):
		# print url
		db = self.get_db()
		cursor = db.cursor()
		cursor.execute("select * from likedimg where url = ?",[url])
		if cursor.fetchone() == None :
			db.execute('insert into likedimg (url) values (?)',[url])
			db.commit()
			return True
		else:
			return False

	def show(self):
		db = self.get_db()
		cursor = db.cursor()
		cursor.execute('select * from likedimg')
		result = cursor.fetchall()
		tem = list(result)
		output=[]
		for (num, url) in tem:
			output.append(url)		
		return output
	
	def delete(self,url):
		# print url
		db = self.get_db()
		db.execute("delete from likedimg where url = ?",[url])
		db.commit()
		return True

