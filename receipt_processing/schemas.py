from flask_restx import fields, Namespace


api = Namespace('receipts', description='Receipt related operations')

item_model = api.model('Item', {
    'shortDescription': fields.String(required=True, description='The item description'),
    'price': fields.String(required=True, description='The item price')
})

receipt_request_model = api.model('Receipt', {
    'retailer': fields.String(required=True, description='The retailer name'),
    'purchaseDate': fields.String(required=True, description='The purchase date'),
    'purchaseTime': fields.String(required=True, description='The purchase time'),
    'items': fields.List(fields.Nested(item_model), required=True, description='List of items in the receipt'),
    'total': fields.String(required=True, description='The total amount of the receipt'),
})

receipt_response_model = api.model('Receipt', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a receipt'),
    'retailer': fields.String(required=True, description='The retailer name'),
    'purchaseDate': fields.String(required=True, description='The purchase date'),
    'purchaseTime': fields.String(required=True, description='The purchase time'),
    'items': fields.List(fields.Nested(item_model), required=True, description='List of items in the receipt'),
    'total': fields.String(required=True, description='The total amount of the receipt'),
    'points': fields.Integer(description='Points assigned to the receipt')
})
