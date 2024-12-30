from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import db
from models.employee import Employee
from models.production import Production
from models.product import Product
from models.order import Order
from models.customer import Customer

def get_total_quantity_by_employee():
    with Session(db.engine) as session:
        result = session.query(
            Employee.name.label('employee_name'),
            db.func.sum(Production.quantity_produced).label('total_quantity')
        ).join(Production, Employee.id == Production.employee_id) \
        .group_by(Employee.name).all()

        return [{"employee_name": row.employee_name, "total_quantity": row.total_quantity} for row in result]

def get_top_selling_products(limit=10):
    
    with Session(db.engine) as session:
        result = session.query(
            Product.name.label('product_name'),
            func.sum(Order.quantity).label('total_quantity')
        ).join(Order, Product.id == Order.product_id) \
        .group_by(Product.name) \
        .order_by(desc(func.sum(Order.quantity))) \
        .limit(limit) \
        .all()

        return [{"product_name": row.product_name, "total_quantity": row.total_quantity} for row in result]
    
def get_customer_order_totals(threshold=0):
    with Session(db.engine) as session:
        result = session.query(
            Customer.name.label('customer_name'),
            func.sum(Order.total_price).label('total_order_value')
        ).join(Order, Customer.id == Order.customer_id) \
        .group_by(Customer.name) \
        .having(func.sum(Order.total_price) >= threshold) \
        .order_by(desc(func.sum(Order.total_price))) \
        .all()

        return [
            {
                "customer_name": row.customer_name,
                "total_order_value": row.total_order_value
            }
            for row in result
        ]

def get_quantity_produced_by_date(specific_date):
    with Session(db.engine) as session:
        # Subquery to filter production records for the specified date
        filtered_production = session.query(Production) \
            .filter(Production.date_produced == specific_date) \
            .subquery()

        # Main query to calculate total quantity produced grouped by product name
        result = session.query(
            Product.name.label('product_name'),
            func.sum(filtered_production.c.quantity_produced).label('total_quantity_produced')
        ).join(
            filtered_production, Product.id == filtered_production.c.product_id
        ).group_by(Product.name).all()

        return [
            {
                "product_name": row.product_name,
                "total_quantity_produced": row.total_quantity_produced
            }
            for row in result
        ]