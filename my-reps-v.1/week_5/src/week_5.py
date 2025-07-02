import csv
# Function to load data from CSV files
def load_data(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Function to save data to CSV files
def save_data(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Load existing data
products = load_data("products.csv")
couriers = load_data("couriers.csv")
orders = load_data("orders.csv")

def menu():
    while True:
        print("\nMain Menu:")
        print("1. Products Menu")
        print("2. Orders Menu")
        print("3. Couriers Menu")
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
                print("3. Delete Product")
                print("0. Return to Main Menu")

                product_choice = input("Enter your choice: ")

                if product_choice == "0":
                    break

                elif product_choice == "1":
                    print("\nProduct List:")
                    if products:
                        for index, product in enumerate(products, start=1):
                            print(f"{index}: {product}")
                    else:
                        print("No products available.")

                elif product_choice == "2":
                    product_name = input("Enter new product name: ")
                    products.append({"name": product_name})
                    save_data("products.csv", products, fieldnames=["name"])# save data 
                    print(f"Product '{product_name}' added successfully!")

                elif product_choice == "3":
                    print("\nProduct List:")
                    for index, product in enumerate(products, start=1):
                        print(f"{index}: {product['name']}")

                    try:
                        remove_index = int(input("Enter the number of the product to remove: ")) - 1
                        if 0 <= remove_index < len(products):
                            removed_product = products.pop(remove_index)
                            save_data("products.csv", products, fieldnames=["name"])
                            print(f"Product '{removed_product['name']}' removed successfully!")
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Invalid input. Please enter a number.") #fixed!

                else:
                     print("No products available to delete.")

#---------------------------------------------------------------------------------------------------------------------------

        elif choice == "2":
            while True:
                print("\nOrders Menu:")
                print("1. View Sample Order")
                print("2. Create New Order")
                print("3. View All Orders")
                print("4. Update Status Of An Order")
                print("0. Return to Main Menu")

                order_choice = input("Enter your choice: ")

                if order_choice == "0":
                    break

                elif order_choice == "1":
                    sample_order = {
                        "name": "Mac",
                        "address": "221B Baker Street",
                        "phone": "116 123"
                    }
                    print(sample_order)

                elif order_choice == "2":
                    customer_name = input("Enter customer name: ")
                    customer_address = input("Enter customer address: ")
                    customer_phone = input("Enter customer phone number: ")

                    new_order = {
                        "name": customer_name,
                        "address": customer_address,
                        "phone": customer_phone,
                    }
                    orders.append(new_order)
                    save_data("orders.csv", orders, fieldnames=["name", "address", "phone", "status"])
                    print("\nCustomer Order Recorded:", new_order)

                elif order_choice == '3':
                    print("\nOrders List:")
                    if orders:
                        for index, order in enumerate(orders, start=1):
                            print(f"{index}: {order}")
                    else:
                        print("Error: No orders available.")

                elif order_choice == '4':
                    print("\nOrders List:")
                    if orders:
                        for index, order in enumerate(orders, start=1):
                            print(f"{index}: {order}")
                            try:
                                order_index = int(input("Enter the order number to update: ")) - 1
                                if 0 <= order_index < len(orders):
                                    new_status = input("Enter new order status (e.g., 'Pending', 'Shipped', 'Delivered'): ")
                                    orders[order_index]['status'] = new_status  # Update status
                                    save_data("orders.csv", orders, fieldnames=["name", "address", "phone", "status"])
                                    print(f"Order status updated successfully to '{new_status}'!")
                                else:
                                    print("Invalid selection.")
                            except ValueError:
                                print("Invalid input. Please enter a valid order number.")
#---------------------------------------------------------------------------------------------------------------------------
        elif choice == "3":
            while True:
                print("\nCouriers Menu:")
                print("1. View Couriers")
                print("2. Add Courier")
                print("0. Return to Main Menu")

                courier_choice = input("Enter your choice: ")

                if courier_choice == "0":
                    break

                elif courier_choice == "1":
                    if couriers:
                        print("\nCourier List:")
                        for index, courier in enumerate(couriers, start=1):
                            print(f"{index}: {courier['name']} - {courier['service']}")

                    else:
                        print("No couriers available.")

                elif courier_choice == "2":
                    courier_name = input("Enter courier name: ")
                    courier_service = input("Enter courier service: ")

                    new_courier = {"name": courier_name, "service": courier_service}
                    couriers.append(new_courier)
                    save_data("couriers.csv", couriers, fieldnames=["name", "service"])
                    print(f"Courier '{courier_name}' added successfully!")

                else:
                    print("Invalid choice, please try again.")
menu()
#PEBKAC-problem exists between keyboard and chair