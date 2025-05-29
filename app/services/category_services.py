from app.db.session import Session
from app.models.category import Category

def create_category(category_name: str):
    session = Session()
    category = Category(
        category_name = category_name
    )
    session.add(category)
    session.commit()
    return category

def get_all_categories():
    session = Session()
    rows = session.query(Category).all()
    session.close()
    return rows

def find_category_by_name(name: str):
    session = Session()
    q = session.query(Category).filter_by(category_name=name).first()
    session.close()
    print(q)
    
    
def delete_category(c_name: str):
    session = Session()
    
    d = find_category_by_name(c_name)
    session.delete(d)
    session.commit
    