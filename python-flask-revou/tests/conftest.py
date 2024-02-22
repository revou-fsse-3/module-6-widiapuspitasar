from app import app
import pytest
from app.utils.database import db
import os


@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.app_context():
        yield app


