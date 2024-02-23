from flask import Flask

from app.controller import animal_route, employees_route
import os
from app.utils.database import db, migrate

app = Flask(__name__)

DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'postgresql' )
DATABASE_NAME = os.getenv('DATABASE_NAME', 'default_database_name')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'default_host')
DATABASE_PORT = os.getenv('DATABASE_PORT', 0)
DATABASE_USER = os.getenv('DATABASE_USER', 'default_user')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'default_password')
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(animal_route.animal_blueprint, url_prefix="/animals")
app.register_blueprint(employees_route.employees_blueprint, url_prefix="/employees")
