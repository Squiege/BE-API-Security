from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), primary_key=False)
    price: Mapped[float] = mapped_column(db.Float, primary_key=False)

    productions: Mapped["Production"] = db.relationship(back_populates="product")
    orders: Mapped["Order"] = db.relationship(back_populates="product")