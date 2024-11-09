from flask import Flask, request, jsonify
import uuid
from utils.points_calculator import calculate_points
from utils.validate import validate_receipt


app = Flask(__name__)

# Alternative to Database, using it with in-memory storage.
# We can also use a cloud storage options such as Firebase which can hold key-value pairs if we need
# this information to persist for long term usage

receipts_key_value_pairs = {}

# Endpoint to process receipts and calculate points
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.json
    if not receipt:
        return jsonify({"error": "Invalid receipt"}), 400

    is_valid, error_message = validate_receipt(receipt)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Generate a unique ID for the receipt
    receipt_id = str(uuid.uuid4())

    # Calculate points based on rules provided
    points = calculate_points(receipt)

    receipts_key_value_pairs[receipt_id] = points

    return jsonify({'id': receipt_id}), 200


# Endpoint to retrieve points for a given receipt ID
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    points = receipts_key_value_pairs.get(receipt_id)
    if points is None:
        return jsonify({"error": "Receipt ID not found"}), 404

    return jsonify({"points": points})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)