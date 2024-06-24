from flask_restx import Resource, reqparse
from .schemas import receipt_request_model, receipt_response_model
from .schemas import api as ns
from .utils import combine_date_time, generate_id
from .models import Receipt

print(f"\n\n\n\n namespace api: {ns}")

class ReceiptResource(Resource):
    def __init__(self, *args, **kwargs):
        self.receipts = kwargs['receipts']

    @ns.expect(receipt_request_model)
    @ns.marshal_with(receipt_response_model, code=201)
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('retailer', type=str, required=True, help='Retailer is required')
        parser.add_argument('purchaseDate', type=str, required=True, help='Purchase date is required')
        parser.add_argument('purchaseTime', type=str, required=True, help='Purchase time is required')
        parser.add_argument('items', type=list, location='json', required=True, help='Items are required')
        parser.add_argument('total', type=float, required=True, help='Total amount is required')

        args = parser.parse_args()

        new_receipt = Receipt(
            retailer = args["retailer"],
            purchase_date = args["purchaseDate"],
            purchase_time = args["purchaseTime"],
            items = args["items"],
            total = args["total"]
        )

        new_receipt.id = generate_id(self.receipts)

        return new_receipt.to_dict(), 201

    def get(self):
        return {"message" : "test"}
