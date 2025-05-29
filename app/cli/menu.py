from app.services.product_services import get_all, create_product, find_by_name, delete_product

def main_menu():
    while True:
        print("\n--- Inventory manager ----")
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
            
            print("Succesfully created product")
            
        elif choice == "2":
            p = input("Enter product name: ")
            search = find_by_name(p)
            
            if search == False:
                print("Product Not Found!")
            else:
                print (search)
                
        elif choice == "3":
            products = get_all()
            for p in products:
                print(p)
        
        elif choice == "4":
            item_to_del = input("Enter ID of Product to Delete: ")
            delete_product(item_to_del)
            
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
        
        
            