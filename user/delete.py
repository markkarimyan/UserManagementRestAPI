from flask import Blueprint, jsonify
from models import db, User
from flask_jwt_extended import jwt_required, get_jwt_identity

user_delete_routes = Blueprint('user_delete_routes', __name__)

@user_delete_routes.route('/users/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    try:
        user_id = get_jwt_identity()
        if user_id != id:
            return jsonify({"error": "Access denied"}), 403

        user = User.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
