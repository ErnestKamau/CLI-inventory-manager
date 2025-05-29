from app.services.category_services import create_category, find_category_by_name, delete_category, get_all_categories


def category_menu():
    while True:
        print("\n ----- CATEGORY MENU -----")
        print("1. Create Category")
        print("2. Find Category")
        print("3. View all Category")
        print("4. Delete Category")
        print("5. Exit")
        
        choice = input("Select an option (1 - 3): ")
        
        if choice == "1":
            c = input("Name of Category: ")
            create_category(category_name=c)
            print("\n Category created Succesfully!")
            
        elif choice =="2":
            f = input("Name of category: ")
            r = find_category_by_name(f)
            if r:
                print(f"\n {r}")
            else:
                print("\n category not found!")
        
        elif choice =="3":
            rows = get_all_categories()
            for z in rows:
                print(f"\n {z}")
                
        elif choice =="4":
            n = input("Name of Category to delete: ")
            delete_category(n)
            
            print("\n Removed Succesfully!")
            
        elif choice == "5":
            break
        
        else:
            print("\n Invalid Choice")
            
            
            