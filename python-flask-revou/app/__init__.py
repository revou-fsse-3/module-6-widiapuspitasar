from flask import Flask
from app.route import animals_route

app = Flask(__name__)

app.register_blueprint(animals_route.animals_blueprint, url_prefix="/animals")
