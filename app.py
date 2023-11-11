from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from dotenv import load_dotenv
from models import db
from flask_jwt_extended import JWTManager
import psycopg2
 
app = Flask(__name__)

#load environment variables
load_dotenv()
 # Load configuration based on the environment (development or production)
 # #Change to ProductionConfig/DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')

CORS(app, supports_credentials=True)
url = app.config('SQLALCHEMY_DATABASE_URI')
connection = psycopg2.connect(url)

#db.init_app(app)   
#with app.app_context():
#    db.create_all()

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)


# Import Blueprints
from blueprints.user.views import user_bp
from blueprints.ride.views import ride_bp
#from blueprints.buddy.views import buddy_bp

# Register Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(ride_bp)
#app.register_blueprint(buddy_bp)


if __name__ == "__main__":
    app.run()