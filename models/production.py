from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

class Production(Base):
    __tablename__ = 'production'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity_produced: Mapped[int] = mapped_column(nullable=False)
    date_produced: Mapped[date] = mapped_column(nullable=False)

    # Relationship
    product: Mapped["Product"] = db.relationship(back_populates="productions")