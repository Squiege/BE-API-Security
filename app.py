# Imports
from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from sqlalchemy.orm import Session

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.production import Production
from models.employee import Employee
from models.role import Role
from models.customerManagementRole import CustomerManagementRole

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.productionBP import production_blueprint
from routes.reportBP import report_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(production_blueprint, url_prefix='/productions')
    app.register_blueprint(report_blueprint, url_prefix='/reports')

def configure_rate_limit():
    limiter.limit("5 per day")(customer_blueprint)

def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                CustomerAccount(username='ctm1', password='1234', customer_id=1),
                CustomerAccount(username='ctm2', password='1234', customer_id=2),
                CustomerAccount(username='ctm3', password='1234', customer_id=3)
            ]

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name='Admin'),
                Role(role_name='Manager'),
                Role(role_name='User')
            ]
            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_customers = [
                CustomerManagementRole(customer_id=1, role_id=1),
                CustomerManagementRole(customer_id=2, role_id=2),
                CustomerManagementRole(customer_id=3, role_id=3)
            ]
            session.add_all(roles_customers)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    
    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_roles_customers_data()
        init_roles_data()
        init_customers_info_data()

    app.run(debug=True)