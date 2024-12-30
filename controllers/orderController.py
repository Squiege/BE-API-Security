from flask import request, jsonify
from models.schemas.orderSchema import order_schema
from services import orderService
from marshmallow import ValidationError

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    order_save = orderService.save(order_data)
    return order_schema.jsonify(order_save), 201