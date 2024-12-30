from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CustomerAccount(Base):
    __tablename__ = 'customer_accounts'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))

    # One to One relationship
    customer: Mapped["Customer"] = relationship("Customer", back_populates="customer_account")

    # One to Many relationship
    roles: Mapped["Role"] = db.relationship(secondary="Customer_Management_Roles")

