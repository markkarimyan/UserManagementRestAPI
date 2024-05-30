from flask import Blueprint, request, jsonify
from models import db, User
from schemas import user_schema, ValidationError

user_update_routes = Blueprint('user_update_routes', __name__)

@user_update_routes.route('/users/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    try:
        user_schema.load(data)
        user = User.query.get(id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500