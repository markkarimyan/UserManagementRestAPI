from flask import Blueprint, request, jsonify
from models import db, User
from schemas import user_schema, ValidationError

user_create_routes = Blueprint('user_create_routes', __name__)

@user_create_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user_schema.load(data)
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500