from app.db.session import Session
from app.models.sale import Sale

def create_sale(employee: str):
    session = Session()
    
    sale = Sale(
        employee_name = employee
    )
    session.add(sale)
    session.commit()
    return sale

def get_all():
    session = Session()
    sales = session.query(Sale).all()
    session.close()
    return sales

def find_sale_by_id(id: int):
    session = Session()
    s = session.query(Sale).filter_by(id=id).first()
    session.close()
    return s

def delete_sale(del_id: int):
    session = Session()
    
    d = find_by_id(del_id)
    if d :
        session.delete(d)
        session.commit()
    return d