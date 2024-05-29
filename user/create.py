from flask import Blueprint, request, jsonify
from models import db, User

user_create_routes = Blueprint('user_create_routes', __name__)

@user_create_routes.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201