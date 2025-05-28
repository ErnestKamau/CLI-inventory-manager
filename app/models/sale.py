from . import Base
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime(), default=datetime.now, nullable=False)
    employee_name = Column(String(), nullable=False)