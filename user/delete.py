from flask import Blueprint, jsonify
from models import db, User

user_delete_routes = Blueprint('user_delete_routes', __name__)

@user_delete_routes.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500