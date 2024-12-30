from sqlalchemy.orm import Session
from database import db
from models.production import Production

def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(name=production_data['name'], description=production_data['description'], price=production_data['price'])
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
        return new_production