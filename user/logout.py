from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from models import db, TokenBlocklist
from datetime import datetime

user_logout_routes = Blueprint('logout_routes', __name__)

@user_logout_routes.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']
        db.session.add(TokenBlocklist(jti=jti, created_at=datetime.utcnow()))
        db.session.commit()
        return jsonify({"message": "Successfully logged out"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
