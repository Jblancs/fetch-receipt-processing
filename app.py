from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from receipt_processing import receipt_bp

app = Flask(__name__)
api = Api(app)
CORS(app)

# In-memory storage for receipts as a dictionary
app.receipts = {}

# blueprints
app.register_blueprint(receipt_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
