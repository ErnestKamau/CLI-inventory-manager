from . import Base
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime(), default=datetime.now, nullable=False)
    employee_name = Column(String(), nullable=False)
    
    sale_items = relationship(
        'SaleItem', 
        backref=backref('sale'),
        cascade="all, delete-orphan"
        )
   
    def __repr__(self):
        formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        return f"<Sale_id={self.id} : date={formatted_date}, employee_name={self.employee_name}>"
