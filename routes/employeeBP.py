from flask import Blueprint
from controllers.employeeController import save

employee_blueprint = Blueprint('employee_bp', __name__)

employee_blueprint.route('/', methods=['POST'])(save)
employee_blueprint.route('/<int:employee_id>', methods=['GET'])(save)
employee_blueprint.route('/employees', methods=['GET'])(save)