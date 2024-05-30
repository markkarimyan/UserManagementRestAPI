from flask import Blueprint, jsonify
from models import User

user_read_routes = Blueprint('user_read_routes', __name__)

@user_read_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        result = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

