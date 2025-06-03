from app.services.category_services import create_category, find_category_by_name, delete_category, get_all_categories, update_category_name


def category_menu():
    while True:
        print("\n ----- CATEGORY MENU -----")
        print("1. Create Category")
        print("2. Find Category")
        print("3. View all Category")
        print("4. Delete Category")
        print("5. Update Category name")
        print("6. Exit")
        
    
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
            
        
        elif choice =="3":
            rows = get_all_categories()
            for z in rows:
                print(f"\n {z}")
                
        elif choice =="4":
            n = input("Name of Category to delete: ")
            delete_category(n)
            
            print("\n Removed Succesfully!")
            
        elif choice == "5":
            category_id = int(input("Enter the Category ID to update: "))
            new_name = input("Enter the new name: ")
            updated = update_category_name(category_id, new_name)
            print("Category updated successfully:")
            print(updated)
            
            
        elif choice == "6":
            break
        
        else:
            print("\n Invalid Choice")
            
            
            