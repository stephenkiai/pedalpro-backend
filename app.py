# Import necessary modules from Flask and other libraries
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from models import db

# Load environment variables from the .env file
load_dotenv()
 
app = Flask(__name__)

# Load configuration settings from the DevelopmentConfig class in the config module
app.config.from_object('config.DevelopmentConfig')

# Enable Cross-Origin Resource Sharing (CORS) with support for credentials
CORS(app, supports_credentials=True)
  
# Set the SQLAlchemy database URI for connecting to PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pgqulwdclzedha:48eb104fc363ee75a99131a6b684b36758bc7fbaf87d0f8490652749b1edebd3@ec2-44-215-40-87.compute-1.amazonaws.com:5432/dc0egqt2llo2uo'


# Initialize the SQLAlchemy database with the Flask app
db.init_app(app)

# Create all database tables within the app context
with app.app_context():
    db.create_all()

# Configure the JWT secret key for token generation and validation
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)


# Import Blueprints for modularizing routes
from blueprints.user.views import user_bp
from blueprints.ride.views import ride_bp


# Register Blueprints with the main app
app.register_blueprint(user_bp)
app.register_blueprint(ride_bp)


# Run the app if this script is executed
if __name__ == "__main__":
    app.run()