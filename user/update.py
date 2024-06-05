from flask import Blueprint, request, jsonify
from models import db, User
from schemas import user_schema, ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash

user_update_routes = Blueprint('user_update_routes', __name__)

@user_update_routes.route('/users/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.get_json()
    try:
        user_schema.load(data)
        user_id = get_jwt_identity()
        if user_id != id:
            return jsonify({"error": "Access denied"}), 403

        user = User.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        user.name = data['name']
        user.email = data['email']
        user.password = generate_password_hash(data['password'])
        role = data['role']
        if role not in User.ROLES:
            return jsonify({"error": "Invalid role"}), 400
        user.role = role
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
