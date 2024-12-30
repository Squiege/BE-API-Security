from flask import Blueprint, jsonify, request
from services.reportService import get_total_quantity_by_employee, get_top_selling_products, get_customer_order_totals, get_quantity_produced_by_date

# Report Blueprint
report_blueprint = Blueprint('report_bp', __name__)

@report_blueprint.route('/employee-production', methods=['GET'])
def employee_production_summary():
    try:
        result = get_total_quantity_by_employee()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@report_blueprint.route('/top-selling-products', methods=['GET'])
def top_selling_products():
    try:
        limit = request.args.get('limit', default=10, type=int)
        result = get_top_selling_products(limit)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@report_blueprint.route('/customer-order-totals', methods=['GET'])
def customer_order_totals():
    try:
        threshold = request.args.get('threshold', default=0, type=float)
        result = get_customer_order_totals(threshold)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@report_blueprint.route('/production-quantity', methods=['GET'])
def production_quantity():
    try:
        specific_date = request.args.get('date', type=str)
        if not specific_date:
            return jsonify({"error": "Date parameter is required."}), 400
        
        result = get_quantity_produced_by_date(specific_date)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500