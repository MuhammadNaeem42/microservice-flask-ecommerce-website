# application/order_api/__init__.py
from flask import Blueprint

order_api_blueprint = Blueprint('order_api', __name__)

from . import routes