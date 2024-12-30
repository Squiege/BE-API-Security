from flask import Blueprint
from controllers.customerController import save

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/<int:id>', methods=['GET'])(save)
customer_blueprint.route('/customers', methods=['GET'])(save)