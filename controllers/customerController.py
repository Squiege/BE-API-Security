from flask import request, jsonify
from models.schemas.customerSchema import customer_schema
from services import customerService
from marshmallow import ValidationError

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    customer_save = customerService.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({"message": "Customer not saved"}), 400
    
    @token_required
    @role_required("admin")
    def find_all():
        customers = customerService.find_all()
        return customer_schema.jsonify(customers), 200