from sqlalchemy.orm import Session
from database import db
from models.employee import Employee
from sqlalchemy import func
from models.production import Production

def save(employee_data):
    with Session(db.engine) as session:
        with session.begin():
            new_employee = Employee(name=employee_data['name'], email=employee_data['email'], phone=employee_data['phone'])
            session.add(new_employee)
            session.commit()

        session.refresh(new_employee)
        return new_employee
    
def get_total_quantity_by_employee():
    result = db.session.query(
        Employee.name,
        func.sum(Production.quantity_produced).label('total_quantity')
    ).join(
        Production, Production.employee_id == Employee.id
    ).group_by(
        Employee.name
    ).all()

    return result


