from flask import Blueprint, request, jsonify
from controllers.productController import save
from services.productService import get_paginated_products, get_product_by_id

product_blueprint = Blueprint('product_bp', __name__)

# Create a new product
@product_blueprint.route('/', methods=['POST'])
def create_product():
    return save()

# Fetch a single product by its ID
@product_blueprint.route('/<int:product_id>', methods=['GET'])
def fetch_product_by_id(product_id):
    return get_product_by_id(product_id)

# Fetch all products with pagination
@product_blueprint.route('/', methods=['GET'])
def get_products():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    result = get_paginated_products(page, per_page)
    return jsonify(result)
