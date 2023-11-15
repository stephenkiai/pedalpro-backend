""" views/routes for the user blueprint """
from flask import jsonify, request, Blueprint
from models import db, Users, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from constants import ROLES
import hashlib, uuid
from flask_jwt_extended import create_access_token
from datetime import timedelta


# Initialize the UserSchema for serialization
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a Flask Blueprint for user-related routes
user_bp = Blueprint('user', __name__)


# User registration route
@user_bp.route('/register',methods=['POST'])
def register_user():
    """ Extract user data from the request JSON """
    name = request.json['name']
    email = request.json['email']
    plain_password = request.json['password']
    role = request.json['role']

    # Check if the provided role is valid
    if role not in ROLES.values():
        return jsonify({"error": "Invalid role"}), 400
    
    # Check if email/name already exists in database
    existing_user_by_email = Users.query.filter_by(email=email).first()
    existing_user_by_name = Users.query.filter_by(name=name).first()

    if existing_user_by_email:
        return jsonify({"error": "User with this email already exists"}), 400

    if existing_user_by_name:
        return jsonify({"error": "Username is already taken"}), 400
    
     # Generate a unique ID for the new user
    id = str(uuid.uuid4())

    # Hash password
    hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()

    # new user object with provided data
    new_user = Users(id=id, name=name, email=email, password=hashed_password, role=role)

     # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


 # User login route
@user_bp.route('/login', methods=['POST'])
def login_user():
    """ Extract login credentials from the request JSON """
    login_identifier = request.json['login_identifier']
    plain_password = request.json['password']

    # Check if login_identifier exists in either email or name
    user = Users.query.filter((Users.email == login_identifier) | (Users.name == login_identifier)).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Check password
    if hashlib.sha256(plain_password.encode()).hexdigest() != user.password:
        return jsonify({"error": "Invalid password"}), 400

    # Create an access token with the user's ID and role
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))

    # Retrieve user's role
    user_role = user.role

    # Authentication success
    return jsonify({"message": "Authentication successful", "access_token": access_token}), 200


# Route to get user data
@user_bp.route('/user-data', methods=['GET'])
@jwt_required()
def get_user_data():
    # Get user's ID from the JWT token
    user_id = get_jwt_identity()


     # Retrieve user data from the database
    user = Users.query.get(user_id)

    if user:
        # Return user data
        user_data = {
            "userid": user.id,
            "role": user.role
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Route to get all users
@user_bp.route('/users', methods=['GET']) 
def all_users():
    """   Retrieve all users from the database """
    all_users = Users.query.all()

    """  Serialize and return the user data """
    results = users_schema.dump(all_users)
    return jsonify(results)

  
# Route to get user details by ID
@user_bp.route('/profile/<id>',methods =['GET'])
def userdetails(id):
    """ Retrieve user details by ID from the database """
    user = Users.query.get(id)
    return user_schema.jsonify(user)

  
# Route to update user information by ID
@user_bp.route('/update/<id>',methods = ['PUT'])
def userupdate(id):
    """ Retrieve the user by ID from the database """
    user = Users.query.get(id)

    """ Extract updated user data from the request JSON """
    name = request.json['name']
    email = request.json['email']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']

    """ Update user information """
    user.name = name
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.location = location

    """ Commit the changes to the database """
    db.session.commit()
    return user_schema.jsonify(user)

 
 # Route to delete a user by ID
@user_bp.route('/userdelete/<id>',methods=['DELETE'])
def userdelete(id):
    """ Retrieve the user by ID from the database """
    user = Users.query.get(id)

    """ Delete the user from the database """
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
  
