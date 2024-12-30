from sqlalchemy.orm import Session
from database import db
from models.product import Product


def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
        return new_product


def get_paginated_products(page, per_page):
    try:
        # Paginate query results
        paginated_query = db.session.query(Product).paginate(page=page, per_page=per_page, error_out=False)

        products = [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price
            }
            for product in paginated_query.items
        ]

        return {
            "products": products,
            "page": paginated_query.page,
            "per_page": paginated_query.per_page,
            "total_pages": paginated_query.pages,
            "total_items": paginated_query.total
        }
    except Exception as e:
        raise Exception(f"Error fetching paginated products: {e}")


def get_product_by_id(product_id):
    try:
        product = db.session.query(Product).filter_by(id=product_id).first()

        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")

        return {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
    except Exception as e:
        raise Exception(f"Error fetching product by ID: {e}")
