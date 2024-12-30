from marshmallow import fields
from schema import ma
from models import Product  

class ProductionSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_id = fields.Integer(required=True)  
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)

    # Define relationships (Foreign Key references)
    product = fields.Nested('ProductSchema', only=['id', 'name'])  

    class Meta:
        fields = ('id', 'product_id', 'quantity_produced', 'date_produced', 'product')
        ordered = True  

production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)