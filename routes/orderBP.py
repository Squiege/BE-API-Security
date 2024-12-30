from flask import Blueprint, request, jsonify
from controllers.orderController import save
from services.orderService import get_paginated_orders, get_order

order_blueprint = Blueprint('order_bp', __name__)

# Route to create a new order
order_blueprint.route('/', methods=['POST'])(save)

# Route to retrieve a single order by ID
@order_blueprint.route('/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):  
    try:
        order = get_order(order_id) 
        if order:
            return jsonify(order), 200
        else:
            return jsonify({"message": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to retrieve paginated orders
@order_blueprint.route('/', methods=['GET'])
def get_orders():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    result = get_paginated_orders(page, per_page)
    return jsonify(result)
