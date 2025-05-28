from . import Base
from sqlalchemy import Integer, String, Column, Float, ForeignKey

class SaleItem(Base):
    __tablename__ = 'sale_items'
    
    id = Column(Integer(), primary_key=True)
    quantity = Column(Integer(), nullable=False)
    unit_price = Column(Float(), nullable=False)
    sale_id = Column(Integer(), ForeignKey('sales.id'))
    product_id = Column(Integer(), ForeignKey('products.id'))
    
    def __repr__(self):
        return f"<SaleItem {self.id} : quantity={self.quantity}, price={self.unit_price}, sale_id={self.sale_id}, product_id={self.product_id}"