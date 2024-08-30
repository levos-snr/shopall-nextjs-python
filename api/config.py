from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os




# init
app = Flask(__name__)
CORS(app)


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#instance of db
db = SQLAlchemy(app)
migrate = Migrate(app, db)