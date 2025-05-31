from app.services.product_services import get_all, create_product, find_by_name, delete_product
from app.services.sale_services import create_sale, get_all_sales,delete_sale, find_sale_by_id
from app.cli.category_menu import category_menu
from app.services.sale_item_services import create_sale_item
from app.cli.sale_item_menu import sale_items

def products_menu():
    while True:
        print("\n ----- PRODUCTS MENU -----")
        print("1. Add Product")
        print("2. Search For Product by Name")
        print("3. View all Products")
        print("4. Delete product(By ID)")
        print("5. Exit")
                
        choice = input("Select an option 1 - 3: ")
                
        if choice == "1":
            name = input("Name of the product: ")
            price = input("Price of product: ")
            stock_quantity = input("Quantity of Product in Stock: ")
            category_id = input("Category ID of Product: ")
            product = create_product(product_name=name, price=price, stock_quantity=stock_quantity, category_id=category_id)
                    
            print("\n Succesfully created product")
                    
        elif choice == "2":
            p = input("Enter product name: ")
            search = find_by_name(p)
            if search:
                print (f"\n {search}")
            else:
                print("\n Product Not Found!")
        
                            
        elif choice == "3":
            products = get_all()
            for p in products:
                print(f"\n {p}")
                
        elif choice == "4":
            item_to_del = input("Enter ID of Product to Delete: ")
            delete_product(item_to_del)
            
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Try again.")
            
           
            
def add_sale_items(sale_id):
    while True:
        print("\n ----- CREATE SALE ITEMS-----")
        product_id = input("Product ID: ")
        quantity = int(input("Quantity: "))
        unit_price = input("Price (per unit): ")
        
        
        create_sale_item(quantity=quantity, unit_price=unit_price, product_id=product_id, sale_id=sale_id)
        print("\n Successfully created Sale item")
        
        prompt = input("Add another sale item (y/n): ").lower()
        if prompt != 'y':
            break         
            
            
def sale():
    while True:
        print("\n--- SALES MENU ----")
        print("1. Create a Sale")
        print("2. View all Sales")
        print("3. Search for Sale (By_id)")
        print("4. Delete sale")
        print("5. Exit")
        
        c = input("Select an option (1 - 5): ")
        
        if c == "1":
            name = input("Name of employee: ")
            new_sale = create_sale(name)
            print("Sale created successfully!")
            print(f"\nThe sale id of this sale is {new_sale.id}")
            print("\nProceed to add the sale items:")
            
            add_sale_items(new_sale.id)
            
            
            
        elif c == "2":
            sales = get_all_sales()
            for x in sales:
                print (f"\n {x}")
                
        elif c == "3":
            sale_id = input("Enter the Sale ID: ")
            q = find_sale_by_id(sale_id)
            if q:
                print(f"\n {q}")
            else:
                print("Sale not Found!")
                
        elif c == "4":
            sale_to_del = input("Enter ID of Sale to be Deleted: ")
            delete_sale(sale_to_del)
            
        elif c == "5":
            break
        
        else:
            print("Invalid Choice Try again!")
        





def main_menu():
    while True:
        print("\n--- Inventory manager ----")
        print("1. Categories")
        print("2. Products")
        print("3. Sale")
        print("4. Sale Items")
        print("5. Exit")
        
        first_choice = input("Select an option 1 - 4: ")
        
        if first_choice == "1":
            category_menu()
        
        elif first_choice == "2":
            products_menu()
            
        elif first_choice == "3":
            sale()
            
        elif first_choice == "4":
            sale_items()
        
        elif first_choice == "5":
            break
            
            
            
        
        
        
        
        
        
        
        
        
            