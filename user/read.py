from flask import Blueprint, jsonify
from models import User

user_read_routes = Blueprint('user_read_routes', __name__)

@user_read_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users]), 200