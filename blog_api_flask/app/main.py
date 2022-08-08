from app.rest_api.factory import create_app
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

app = create_app()
app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['MONGO_URI'] = config['PROD']['DB_URI']
