from flask import Blueprint, jsonify
from decorator import role_required
from models import Project, User
from flask_jwt_extended import jwt_required, get_jwt_identity

project_read_routes = Blueprint('project_read_routes', __name__)

@project_read_routes.route('/projects', methods=['GET'])
@jwt_required()
@role_required(allow_ceo=True)  # Allow CEO to access everyone's projects
def get_projects():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user.role == 'CEO':
            projects = Project.query.all()
        else:
            projects = Project.query.filter_by(user_id=user_id).all()

        result = [{"id": project.id, "title": project.title, "description": project.description} for project in projects]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@project_read_routes.route('/projects/<int:id>', methods=['GET'])
@jwt_required()
@role_required(allow_ceo=True)  # Allow CEO to access any project
def get_project(id):
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user.role == 'CEO':
            project = Project.query.get(id)
        else:
            project = Project.query.filter_by(id=id, user_id=user_id).first()

        if project is None:
            return jsonify({"error": "Project not found"}), 404

        result = {"id": project.id, "title": project.title, "description": project.description}
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
