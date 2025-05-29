from . import Base
from sqlalchemy import Integer, String, Column, CheckConstraint
from sqlalchemy.orm import relationship, backref

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer(), primary_key=True)
    category_name = Column(String(), index=True)
    
    products = relationship('Product', backref=backref('category'))
    
    def __repr__(self):
        return f"<Category: id={self.id}, category name={self.category_name}>"