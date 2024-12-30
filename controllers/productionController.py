from flask import request, jsonify
from models.schemas.productionSchema import production_schema
from services import productionService
from marshmallow import ValidationError

def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    production_save = productionService.save(production_data)
    return production_schema.jsonify(production_save), 201