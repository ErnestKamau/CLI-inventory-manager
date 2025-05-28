from . import Base
from sqlalchemy import Integer, String, Float, ForeignKey, Column

class Product(Base):
    __tablename__ = 'products'
   
    id = Column(Integer(), primary_key=True)
    product_name = Column(String(), index=True)
    price = Column(Float(), default=0)
    stock_quantity = Column(Integer(), default=0)
    category_id = Column(Integer(), ForeignKey('categories.id'))
    
    
    def __repr__(self):
        return f"<Product {self.id}: {self.product_name}, {self.price}, {self.stock_quantity}, FK: {self.category_id}"