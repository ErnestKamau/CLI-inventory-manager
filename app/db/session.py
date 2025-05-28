from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///app/db/inventory.db')
Session = sessionmaker(bind=engine)
# session = Session()