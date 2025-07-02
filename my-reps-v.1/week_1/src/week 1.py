def menu():         #week 1 coffeee menu 
    products=["latte","cappuccino","white coffee","tea"]
    
    while True:
        print("\nMain Menu:")
        print("1. Products Menu")
        print("2. Orders Menu")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Exiting application...")
            break
        
        elif choice == "1":
            while True:
                print("\nProducts Menu:")
                print("1. View Products")
                print("2. Add Product")
                print("0. Return to Main Menu")
                
                product_choice = input("Enter your choice: ")
                
                if product_choice == "0":
                    break
                
                elif product_choice == "1":
                    print("\nProduct List:")
                    if products:
                        for index, product in enumerate(products):
                            print(f"{index}: {product}")
                    else:
                        print("No products available.")
                
                elif product_choice == "2":
                    product_name = input("Enter new product name: ")
                    products.append(product_name)
                    print(f"Product '{product_name}' added successfully!")
                else:
                    print("Invalid choice, please try again.")
        
# week 2 orders menu
        elif choice == 2: 
                print("\n Welcome to the orders menu")
                
                print ("\n Orders menu")
                print ("1. Order's dictionary")
                print ("2. Customer input")
                print ("0. Exit menu") 
                product_choice = input("Enter your choice: ")
                
                if choice == "0":
                    print ("Closing menu") 
                    break
                
                elif choice == "1":
                    userdict_1= {
                    "name": "mac",
                    "address": "221b baker street",
                    "number": "116 123"
    }
        userdict_2= {
        "user name": userdict_1["name"],
        "user address": userdict_1["address"],
        "user phone number": userdict_1["number"]
    
    }
    print (userdict_2)

menu()
#PEBKAC-problem exists between keyboard and chair