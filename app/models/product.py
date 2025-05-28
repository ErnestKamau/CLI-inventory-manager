from . import Base
from sqlalchemy import Integer, String, Float, ForeignKey, Column
from sqlalchemy.orm import relationship, backref

class Product(Base):
    __tablename__ = 'products'
   
    id = Column(Integer(), primary_key=True)
    product_name = Column(String(), index=True)
    price = Column(Float(), default=0)
    stock_quantity = Column(Integer(), default=0)
    category_id = Column(Integer(), ForeignKey('categories.id'))
    
    sale_items = relationship(
        'SaleItem',
        backref=backref('product'),
        cascade="all, delete-orphan"
    )
    
    
    def __repr__(self):
        return f"<Product {self.id}: name={self.product_name}, price={self.price}, stock_quantity={self.stock_quantity}, FK: {self.category_id}"