from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
from models import db
from flask_jwt_extended import JWTManager
import psycopg2

load_dotenv()
 
app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

CORS(app, supports_credentials=True)

#db.init_app(app)   
#with app.app_context():
#   db.create_all()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pgqulwdclzedha:48eb104fc363ee75a99131a6b684b36758bc7fbaf87d0f8490652749b1edebd3@ec2-44-215-40-87.compute-1.amazonaws.com:5432/dc0egqt2llo2uo'
db = SQLAlchemy(app)

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