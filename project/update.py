from flask import Blueprint, request, jsonify
from decorator import role_required
from models import db, Project, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import project_schema, ValidationError

project_update_routes = Blueprint('project_update_routes', __name__)

@project_update_routes.route('/projects/update/<int:id>', methods=['PUT'])
@jwt_required()
@role_required(allow_ceo=True)  # Allow CEO to update any project
def update_project(id):
    data = request.get_json()
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user.role == 'CEO':
            project = Project.query.get(id)
        else:
            project = Project.query.filter_by(id=id, user_id=user_id).first()

        if project is None:
            return jsonify({"error": "Project not found"}), 404

        project.title = data['title']
        project.description = data.get('description')
        db.session.commit()
        return jsonify({"message": "Project updated successfully"}), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
