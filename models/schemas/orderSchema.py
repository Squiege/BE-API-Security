from marshmallow import fields
from schema import ma
from models import Customer, Product  # Assuming your models are imported here

class OrderSchema(ma.Schema):
    # Define fields manually
    id = fields.Integer(dump_only=True)
    customer_id = fields.Integer(required=True)  
    product_id = fields.Integer(required=True)  
    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=True)

    # Define relationships (Foreign Key references)
    customer = fields.Nested('CustomerSchema', only=['id', 'name']) 
    product = fields.Nested('ProductSchema', only=['id', 'name'])  

    class Meta:
        fields = ('id', 'customer_id', 'product_id', 'quantity', 'total_price', 'customer', 'product')
        ordered = True  

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

