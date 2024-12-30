from sqlalchemy.orm import Mapped, mapped_column
from database import db, Base

class CustomerManagementRole(Base):
    __tablename__ = 'customer_management_roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_management_id: Mapped[str] = mapped_column(db.ForeignKey('Customer_Accounts.id'))
    role_id: Mapped[str] = mapped_column(db.ForeignKey('roles.id'))