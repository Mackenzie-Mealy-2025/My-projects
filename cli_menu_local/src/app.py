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

def menu():          #menu1
    while True:
        print("\nMain Menu:")
        print("1.Print Chicken List.")
        print("2.Create New Chicken Record.")
        print("3.Update Existing Chicken Record.")
        print("4.Delete A Existing Chicken Record.")
        print("0.Exit.")
        
        option = input("Enter your choice: ")
        
        if option == "0":
            print("Exiting application...")
            break
        
        elif option == "1":
            while True:
                print("\Printing Chicken List:")
                if option:
                    for index, product in enumerate(option, start=1):
                            print(f"{index}: {product}")
                    else:
                        print("No products available.")
                        
#---------------------------------------------------------------------------------------------------------------------------
        elif option == "2":
                    chicken_record = input("Enter new product name: ")
                    option.append({"name": chicken_record})
                    save_data("chicken_record.csv", option, fieldnames=["name"])# save data 
                    print(f"Product '{chicken_record}' added successfully!")

                
#---------------------------------------------------------------------------------------------------------------------------
        elif option =="3":
            print("Update functionality not implemented yet.")#change


#---------------------------------------------------------------------------------------------------------------------------
        elif option == "4":
                    print("\nProduct List:")
                    for index, product in enumerate(chicken_record, start=1):
                        print(f"{index}: {product['name']}")

                    try:
                        remove_index = int(input("Enter the number of the product to remove: ")) - 1
                        if 0 <= remove_index < len(chicken_record):
                            removed_product = chicken_record.pop(remove_index)
                            save_data("chicken_record.csv", chicken_record, fieldnames=["name"])
                            print(f"Product '{removed_product['name']}' removed successfully!")
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Invalid input. Please enter a number.") #fixed!

                    else:
                     print("No products available to delete.")