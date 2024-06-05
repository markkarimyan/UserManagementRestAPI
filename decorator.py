from functools import wraps
from flask import request, jsonify
from models import User
from flask_jwt_extended import get_jwt_identity

def role_required(allow_ceo=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404

            # Allow CEO to access all resources if allow_ceo is True
            if user.role == 'CEO' and allow_ceo:
                return f(*args, **kwargs)

            # Otherwise, only allow access to the user's own resources
            if 'id' in kwargs and kwargs['id'] == user_id:
                return f(*args, **kwargs)

            # Restrict access if not CEO and accessing other user's resources
            if user.role != 'CEO' and not allow_ceo:
                return jsonify({"error": "Access denied"}), 403

            return f(*args, **kwargs)

        return decorated_function
    return decorator
