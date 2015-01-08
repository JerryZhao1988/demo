CONTENTS OF THIS FILE
---------------------

 * Environment
 * Database requirment
 * Starting the app


 Environment
 -----------

 App should run under virtualenv, and I have export my
 venv setting in env_requirment.txt

 Then export the setting path:
 export FLASKR_SETTINGS=~/"path to app"/settings.py


 Database requirment
 -------------------

 sqlite3 is used in this app
 If user's flask have "app.cli.command" script, it would setup
 the database named "demo.db" automatelly.
 Just uncomment three lines below in demo.py

 # @app.cli.command('init_db')
 # def initdb_command():
 # 	DA.initdb() 

 Otherwise, user need to build the 'demo.db' himself, and import 
 schema.sql to initial it.


 Starting the app
 ---------------

 When user finished all those settings, app can starting easily.

 $ python demo.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader

 APP can be visited at "127.0.0.1:5000" or "publicIP:5000"











