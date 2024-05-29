from flask import Blueprint, request, jsonify
from models import db, User

user_update_routes = Blueprint('user_update_routes', __name__)

@user_update_routes.route('/users/update/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200