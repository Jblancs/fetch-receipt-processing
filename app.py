from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from receipt_processing import receipt_bp
# from receipt_processing.resources import ReceiptResource

app = Flask(__name__)
CORS(app)

# In-memory storage for receipts as a dictionary
# app.receipts = {}

# blueprints
app.register_blueprint(receipt_bp, url_prefix='/receipts')

# api.add_resource(ReceiptResource, '/', '/test',
#                  resource_class_kwargs={'receipts': app.receipts})

if __name__ == '__main__':
    app.run(debug=True)
