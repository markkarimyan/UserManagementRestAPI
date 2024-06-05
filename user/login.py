from flask import Blueprint, request, jsonify
from models import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

user_login_routes = Blueprint('user_login_routes', __name__)

@user_login_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
