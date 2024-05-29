from flask import Flask
from config import Config
from models import db
from create import user_create_routes
from read import user_read_routes
from update import user_update_routes


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(user_create_routes)
app.register_blueprint(user_read_routes)
app.register_blueprint(user_update_routes)