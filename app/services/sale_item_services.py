from app.db.session import Session
from app.models.sale_item import SaleItem
from app.models.product import Product



def create_sale_item(quantity: int, unit_price: float, sale_id: int,  product_id: int):
    session = Session()
    
    product = session.query(Product).filter_by(id=product_id).first()
    if not product:
        raise ValueError("Product not found")
    
    product.stock_quantity -= quantity


    item_for_sale = SaleItem(
        quantity=quantity,
        unit_price=unit_price,
        sale_id=sale_id,
        product_id=product_id
    )
    
    session.add(item_for_sale)
    session.commit()
    

def get_all_sale_items():
    session = Session()
    items = session.query(SaleItem).all()
    session.close()
    
    return items

def find_by_id(id: int):
    session = Session()
    item = session.query(SaleItem).filter_by(id=id).first()
    session.close()
    
    return item

def get_product_name(id: int):
    session = Session()
    i = find_by_id(id)
    r = i.product_id
    p = session.query(Product).filter_by(id=r).first()
    session.close()
    
    p_name = p.product_name
    
    return p_name


def delete_sale_item(id: int):
    session = Session()
    x = find_by_id(id)
    session.delete(x)
    session.commit()  
    