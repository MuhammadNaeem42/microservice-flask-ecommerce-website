# application/user_api/__init__.py
from flask import Blueprint

user_api_blueprint = Blueprint('user_api', __name__)

from . import routes
