from flask import Blueprint, request, jsonify
from models import db, Project
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import ValidationError

project_create_routes = Blueprint('project_create_routes', __name__)

@project_create_routes.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    data = request.get_json()
    try:
        user_id = get_jwt_identity()
        new_project = Project(
            title=data['title'],
            description=data.get('description'),
            user_id=user_id
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"message": "Project created successfully"}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
