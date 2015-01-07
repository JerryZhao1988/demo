import flask
import os
import sqlite3
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import g


class Database(object):
	def __init__(self,path):
		self.path = path


	def connect_db(self):
		rv = sqlite3.connect(self.path)
		rv.row_factory = sqlite3.Row
		return rv

	def init_db(self):
		db = self.get_db()
		with app.open_resource('schema.sql', mode= 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()


	def add(self,url):
		print url
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
		print url
		db = self.get_db()
		db.execute("delete from likedimg where url = ?",[url])
		db.commit()
		return True

	def initdb(self):
		self.init_db()
		print('Initialized the database')

	def get_db(self):
	    """Opens a new database connection if there is none yet for the
	    current application context.
	    """
	    if not hasattr(g, 'sqlite_db'):
	        g.sqlite_db = self.connect_db()
	    return g.sqlite_db

	def close(self,error):
		"""Closes the database again at the end of the request."""
		if hasattr(g, 'sqlite_db'):
			g.sqlite_db.close()	 


