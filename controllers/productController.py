from flask import request, jsonify
from models.schemas.productSchema import product_schema
from services import productService
from marshmallow import ValidationError
from services.productService import get_product_by_id

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    product_save = productService.save(product_data)
    return product_schema.jsonify(product_save), 201

def fetch_product_by_id(product_id):
    try:
        product = get_product_by_id(product_id)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {e}"}), 500