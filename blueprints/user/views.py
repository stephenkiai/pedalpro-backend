from flask import jsonify, request, Blueprint
from models import db, Users, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from constants import ROLES
import hashlib, uuid
from flask_jwt_extended import create_access_token
from datetime import timedelta



user_schema = UserSchema()
users_schema = UserSchema(many=True)


user_bp = Blueprint('user', __name__)

@user_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@user_bp.route('/register',methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    plain_password = request.json['password']
    role = request.json['role']

    if role not in ROLES.values():
        return jsonify({"error": "Invalid role"}), 400
    
    # Check if email/name already exists in database
    existing_user_by_email = Users.query.filter_by(email=email).first()
    existing_user_by_name = Users.query.filter_by(name=name).first()

    if existing_user_by_email:
        return jsonify({"error": "User with this email already exists"}), 400

    if existing_user_by_name:
        return jsonify({"error": "Username is already taken"}), 400
    
    id = str(uuid.uuid4())

    # Hash password
    hashed_password = hashlib.sha256(plain_password.encode()).hexdigest()

    # new user object with provided data
    new_user = Users(id=id, name=name, email=email, password=hashed_password, role=role)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

 
@user_bp.route('/login', methods=['POST'])
def login_user():
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


# Endpoint to get user data
@user_bp.route('/user-data', methods=['GET'])
@jwt_required()
def get_user_data():
    # Get user's ID from the JWT token
    user_id = get_jwt_identity()


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


@user_bp.route('/users', methods=['GET']) 
def all_users():
    all_users = Users.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)

  
@user_bp.route('/profile/<id>',methods =['GET'])
def userdetails(id):
    user = Users.query.get(id)
    return user_schema.jsonify(user)

  
@user_bp.route('/update/<id>',methods = ['PUT'])
def userupdate(id):
    user = Users.query.get(id)
  
    name = request.json['name']
    email = request.json['email']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']
  
    user.name = name
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.location = location
  
    db.session.commit()
    return user_schema.jsonify(user)

 
@user_bp.route('/userdelete/<id>',methods=['DELETE'])
def userdelete(id):
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
  
