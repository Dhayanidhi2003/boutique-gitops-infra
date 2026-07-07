from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS allows your frontend (running on port 80/8080) to talk to this backend safely
CORS(app)

@app.route('/api/products', methods=['GET'])
def get_products():
    # Simulated database response
    products = [
        {"id": 1, "name": "Wireless Headphones", "price": 120.00, "category": "Electronics"},
        {"id": 2, "name": "Smart Watch", "price": 199.50, "category": "Electronics"},
        {"id": 3, "name": "Running Shoes", "price": 85.00, "category": "Fashion"}
    ]
    return jsonify(products)

@app.route('/api/health', methods=['GET'])
def health_check():
    # AWS and Kubernetes will use this endpoint to check if the backend is alive!
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)