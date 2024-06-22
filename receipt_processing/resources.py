from flask_restx import Resource, reqparse
from .schemas import api, receipt_request_model, receipt_response_model
from .utils import combine_date_time, generate_id
from .models import Receipt

print(f"API object: {api}")

class ReceiptResource(Resource):
    def __init__(self, *args, **kwargs):
        self.receipts = kwargs['receipts']

    @api.expect(receipt_request_model)
    @api.marshal_with(receipt_response_model, code=201)
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('retailer', type=str, required=True, help='Retailer is required')
        parser.add_argument('purchaseDate', type=str, required=True, help='Purchase date is required')
        parser.add_argument('purchaseTime', type=str, required=True, help='Purchase time is required')
        parser.add_argument('items', type=list, location='json', required=True, help='Items are required')
        parser.add_argument('total', type=float, required=True, help='Total amount is required')

        args = parser.parse_args()

        datetime_obj = combine_date_time(args["purchaseDate"], args["purchaseTime"])

        new_receipt = Receipt(
            retailer = args["retailer"],
            purchase_datetime = datetime_obj,
            items = args["items"],
            total = args["total"]
        )

        new_receipt.id = generate_id(self.receipts)

        return new_receipt, 201

    def get(self):
        return {"message" : "test"}
