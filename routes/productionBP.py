from flask import Blueprint
from controllers.productionController import save

production_blueprint = Blueprint('production_bp', __name__)

production_blueprint.route('/production', methods=['POST'])(save)
production_blueprint.route('/<int:production_id>', methods=['GET'])(save)
production_blueprint.route('/productions', methods=['GET'])(save)