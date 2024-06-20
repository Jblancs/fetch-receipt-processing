from flask_restx import Api
from flask import Blueprint, current_app
from resources import ReceiptResource

receipt_bp = Blueprint('receipts', __name__)

api = Api(receipt_bp)

api.add_resource(ReceiptResource, '/<int:id>/points', '/',
                 resource_class_kwargs={'receipts': current_app.receipts})
