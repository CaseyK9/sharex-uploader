import os

from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/uploads/')
app.config['DISALLOWED_EXTENSIONS'] = {'exe'}
app.config['RANDOM_STRING_LENGTH'] = 5
with open(".hpass") as hpass:
    app.config['HASHED_PASSWORD'] = hpass.read()  # DON'T COMMIT THIS YOU FUCKING IDIOT
app_options = {}
app.debug = False
app.port = 9000
app.config['SECRET_KEY'] = "\xe3\xe7\x97(vc\xaa\xa6\x9fX\x95\xc4\xeb\xba\x94\xacF\xb9\x9d\xe3\xc2\xf71\xac"

import sharex_uploader.views
