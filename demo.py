import flask
import settings

# Views
from index import Index

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

app.add_url_rule('/', view_func=Index.as_view('index'), methods = ["GET" ,"POST"])
app.debug = True
app.run(host='0.0.0.0')

