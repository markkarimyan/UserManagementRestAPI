from flask import Blueprint, jsonify
from models import User
from flask_jwt_extended import jwt_required, get_jwt_identity

user_read_routes = Blueprint('user_read_routes', __name__)

@user_read_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        result = [{"id": user.id, "name": user.name, "email": user.email, "role": user.role} for user in users]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_read_routes.route('/users/<int:id>', methods=['GET'])
# @jwt_required()
def get_user(id):
    try:
        # user_id = get_jwt_identity()
        # if user_id != id:
        #     return jsonify({"error": "Access denied"}), 403

        user = User.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        result = {"id": user.id, "name": user.name, "email": user.email, "role": user.role}
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
