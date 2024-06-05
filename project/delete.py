from flask import Blueprint, jsonify
from decorator import role_required
from models import db, Project, User
from flask_jwt_extended import jwt_required, get_jwt_identity

project_delete_routes = Blueprint('project_delete_routes', __name__)

@project_delete_routes.route('/projects/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required(allow_ceo=True)  # Allow CEO to delete any project
def delete_project(id):
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user.role == 'CEO':
            project = Project.query.get(id)
        else:
            project = Project.query.filter_by(id=id, user_id=user_id).first()

        if project is None:
            return jsonify({"error": "Project not found"}), 404

        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
