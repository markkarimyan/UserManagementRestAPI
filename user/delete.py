from flask import Blueprint, jsonify
from models import db, User

user_delete_routes = Blueprint('user_delete_routes', __name__)

@user_delete_routes.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200