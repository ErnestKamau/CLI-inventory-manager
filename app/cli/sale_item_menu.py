from app.services.sale_item_services import create_sale_item, get_all_sale_items, find_by_id, get_product_name, delete_sale_item

def sale_items():
    while True:
        print("\n ----- SALE ITEMS MENU -----")
        print("1. Get all Sale Items")
        print("2. Search for Sale Item (By ID)")
        print("3. Get Sale Item's Product name (By ID)")
        print("4. Delete Sale Item")
        print("5. Exit")
        
        choice = input("Select an option(1 - 4): ")
       
        if choice == "1":
            sale_item = get_all_sale_items()
            for i in sale_item:
                print(f"\n {i}")
                
        elif choice == "2":
            prompt = input("Enter Sale Item ID: ")
            s = find_by_id(prompt)
            if prompt:
                print(f" \n {s}")
            else:
                print("Item Not Found!")
                
        elif choice == "3":
            r = int(input("Sale Item ID: "))
            q = get_product_name(r)
            print(f"\n {q}")
            
        elif choice == "4":
            w = input("Enter Sale ID of Sale Item to remove: ")
            f = find_by_id(w)
            if f:
                delete_sale_item(w)
            else:
                print("Item Not Found!")
            
        elif choice == "5":
            break
        
        else:
            print("\n Invalid Choice")