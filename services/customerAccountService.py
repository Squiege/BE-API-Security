from sqlalchemy import select
from models.customer import Customer
from models.customerAccount import CustomerAccount
from database import db
from util import encode_token

def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.engine.execute(query).scalars().all()
    return customer_accounts

def login_customer(username, password):
    user = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username, CustomerAccount.password == password)).scalars_one_or_none())
    role_names = [role.role_name for role in user.roles]
    if user:
        auth_token = encode_token(user.id)
        resp = {
            "status": "success",
            "message": "Successfully logged in.",
            "auth_token": auth_token
        }
        return resp
    else:
        return None