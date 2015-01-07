import os
url = 'https://api.flickr.com/services/feeds/photos_public.gne'
option = "?tags="

feed = url + option

DATABASE=os.path.join(os.path.split(os.path.realpath(__file__))[0], 'demo.db')
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='default'