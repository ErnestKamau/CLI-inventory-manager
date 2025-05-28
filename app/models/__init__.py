from sqlalchemy.orm import declarative_base



Base = declarative_base()


from .category import Category
from .product import Product
from .sale import Sale
from .sale_item import SaleItem