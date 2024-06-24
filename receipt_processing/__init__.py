from flask_restx import Api
from flask import Blueprint
from .schemas import api as ns
from .resources import ReceiptResource

receipt_bp = Blueprint('receipts', __name__)

api = Api(receipt_bp, title="Receipts API", version="1.0", description="Operations for Receipts API")

api.add_namespace(ns)

api.add_resource(ReceiptResource, '/', '/test',
                 resource_class_kwargs={'receipts': {}})

print("\n\n\n\n init api" , api)
