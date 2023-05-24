from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User

user_v1 = Blueprint('user_v1', __name__)

@user_v1.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return {'message': 'User created successfully!'}, 201

@user_v1.route('/login') 
def login():
    data = request.get_json()
    username = data['username']
    user = User.query.filter_by(username=username).first()
    access_token = create_access_token(identity=user.id)
    return {'access_token': access_token}

@user_v1.route('/profile')
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return {
        'username': user.username, 
        'is_admin': user.is_admin
    }