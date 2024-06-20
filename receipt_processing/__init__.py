from flask_restx import Api
from flask import Blueprint
from .resources import api

receipt_bp = Blueprint('receipts', __name__)

api.init_app(receipt_bp)
