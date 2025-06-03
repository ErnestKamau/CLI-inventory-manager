from app.db.session import Session
from app.models.product import Product



def get_all():
    session = Session()
    products = session.query(Product).all()
    session.close()
    return products
    
    
def create_product(product_name: str, price: float, stock_quantity: int, category_id: int):
    session = Session()
    
    product = Product(
        product_name = product_name,
        price = price,
        stock_quantity = stock_quantity,
        category_id = category_id
    )
    session.add(product)
    session.commit()
    

def find_by_id(id: int):
    session = Session()
    p = session.query(Product).filter_by(id=id).first()
    session.close()
    return p
    
def find_by_name(product_name: str):
    session = Session()
    product = session.query(Product).filter_by(product_name=product_name).first()
    session.close()
    return product
    
def delete_product(product_id: int):
    session = Session()
    product = find_by_id(product_id)
    if product:
        session.delete(product)
        session.commit()
    return product

def update_product_name(product_id: int, new_name: str):
    session = Session()
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        raise ValueError(f"Product with ID {product_id} not found.")
    
    product.product_name = new_name
    session.commit()
    return product


def update_product_price(product_id: int, new_price: float):
    session = Session()
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        raise ValueError(f"Product with ID {product_id} not found.")
    
    if new_price < 0:
        raise ValueError("Price cannot be negative.")
    
    product.price = new_price
    session.commit()
    return product

def update_product_quantity(product_id: int, new_quantity: int):
    session = Session()
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        raise ValueError(f"Product with ID {product_id} not found.")
    
    if new_quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    
    product.stock_quantity = new_quantity
    session.commit()
    return product