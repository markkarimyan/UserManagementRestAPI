from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from user.create import user_create_routes
from user.read import user_read_routes
from user.update import user_update_routes
from user.delete import user_delete_routes
from user.login import user_login_routes
from project.create import project_create_routes
from project.read import project_read_routes
from project.update import project_update_routes
from project.delete import project_delete_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(user_create_routes)
app.register_blueprint(user_read_routes)
app.register_blueprint(user_update_routes)
app.register_blueprint(user_delete_routes)
app.register_blueprint(user_login_routes)

app.register_blueprint(project_create_routes)
app.register_blueprint(project_read_routes)
app.register_blueprint(project_update_routes)
app.register_blueprint(project_delete_routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
