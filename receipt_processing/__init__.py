from flask_restx import Api
from flask import Blueprint

receipt_bp = Blueprint('receipts', __name__)
api = Api(receipt_bp)
