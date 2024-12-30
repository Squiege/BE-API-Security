from sqlalchemy.orm import Session
from database import db
from models.order import Order

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'])
            session.add(new_order)
            session.commit()

        session.refresh(new_order)
        return new_order
    
from models.order import Order
from database import db

def get_paginated_orders(page, per_page):
    paginated_orders = Order.query.paginate(page=page, per_page=per_page, error_out=False)
    orders = [
        {
            "id": order.id,
            "customer_id": order.customer_id,
            "product_id": order.product_id,
            "quantity": order.quantity,
            "total_price": order.total_price
        }
        for order in paginated_orders.items
    ]

    return {
        "orders": orders,
        "total": paginated_orders.total,
        "page": paginated_orders.page,
        "pages": paginated_orders.pages,
        "per_page": paginated_orders.per_page
    }

from models.order import Order
from database import db

def get_order(order_id):
    try:
        order = db.session.query(Order).filter(Order.id == order_id).first()
        if order:
            return {
                "id": order.id,
                "customer_id": order.customer_id,
                "product_id": order.product_id,
                "quantity": order.quantity,
                "total_price": order.total_price
            }
        else:
            return None
    except Exception as e:
        raise Exception(f"Error fetching order: {e}")
