from marshmallow import fields
from schema import ma

class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    postition = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'postition')

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)