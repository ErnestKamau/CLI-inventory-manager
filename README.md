# CLI-inventory-manager
Interface: Command-Line Interface (CLI)

- A Python-based Inventory Management System that allows users to manage products, track stock levels, organize categories, and record sales—all from the terminal. Designed with clean OOP principles and a normalized relational schema using SQLAlchemy ORM.


# Features
- Manage categories (Create, Read, Update, Delete)
- Manage products (Create, Read, Update, Delete)
- Record sales and related sale items
- Track inventory and stock quantities
- Built with SQLAlchemy ORM, Alembic for migrations, and a clean modular structure


# DESCRIPTION
- This is a Command-Line Inventory Management System built with Python and SQLAlchemy. It allows users to manage product inventory by organizing items into categories, tracking stock quantities and prices, and recording sales.
- Users can add, view, update, and delete products and categories. They can also record sales, add items to each sale, and view all sales with detailed information.
- The project uses a SQLite database and follows Object-Oriented Programming (OOP) best practices with SQLAlchemy ORM for all data operations.


# This CLI Inventory Management System allows users to:
- Create and manage product categories.

- Track inventory through stock quantity and price.

- Record and view product sales with individual sale items.

- Easily navigate and manage data using CLI menus.



# Getting Started
- Follow these steps to clone and run the project on your machine.

# Prerequisites
Python 3.8 or later
pipenv installed globally

## Setup Instructions
# 1. Clone the repo
git clone https://github.com/your-username/CLI-inventory-manager.git
cd CLI-inventory-manager


# 2. Install dependencies
pipenv install

# 3. Activate virtual environment
pipenv shell

# 4. Run database migrations
- This will create the app/db/inventory.db file and tables.

alembic upgrade head


# 5. Run the CLI app
python app.py

- or

./app.py


## How to Use
- Once the app launches, navigate using the menu prompts.

--- Inventory manager ----
1. Categories
2. Products
3. Sale
4. Exit
Select an option 1 - 4:


# Each menu allows the following:
- View existing entries
- Create new entries
- Update or delete entries
- Record a sale (and select products + quantities)
- View sales 

## Technologies Used
- Python 3
- SQLAlchemy ORM
- SQLite
- Alembic
- Pipenv

## Author
- Ernest
- Student Software Developer @ Flatiron School
- GitHub: github.com/ErnestKamau