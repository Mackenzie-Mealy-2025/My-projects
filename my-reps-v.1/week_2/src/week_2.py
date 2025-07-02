def menu():  # Week 1 Coffee Menu
    products = ["latte", "cappuccino", "white coffee", "tea"]

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

                if product_choice == "0": #reset loop
                    break

                elif product_choice == "1": #prints product list
                    print("\nProduct List:")
                    if products:
                        for index, product in enumerate(products, start=1):
                            print(f"{index}: {product}")
                    else:
                        print("No products available.")

                elif product_choice == "2": #add product
                    product_name = input("Enter new product name: ")
                    products.append(product_name) 
                    print(f"Product '{product_name}' added successfully!")
                else:
                    print("Invalid choice, please try again.")

        # Week 2 Orders Menu
        elif choice == "2": 
            while True:
                print("\nWelcome to the Orders Menu")
                print("\nOrders Menu:")
                print("1. Order's Dictionary")
                print("2. Customer Input")
                print("0. Return to Main Menu")

                order_choice = input("Enter your choice: ")

                if order_choice == "0":
                    print("Returning to Main Menu...") #reset loop to start
                    break

                elif order_choice == "1":  #premade customer input to be displayed
                    userdict_1 = {
                        "name": "mac",
                        "address": "221b baker street", #dictionary one(premade user)
                        "number": "116 123"
                    }
                    print (userdict_1)

                elif order_choice == "2":
                    customer_name = input("Enter customer name: ")
                    customer_address = input("Enter customer address: ") #input user info
                    customer_number = input("Enter customer phone number: ")

                    customer_dict = {
                        "user name": customer_name,
                        "user address": customer_address,  #dictionary two(custom user)
                        "user phone number": customer_number
                    }

                    print("\nCustomer Order Recorded:")
                    print(customer_dict)
                else:
                    print("Invalid choice, please try again.")

menu()
#PEBKAC-problem exists between keyboard and chair