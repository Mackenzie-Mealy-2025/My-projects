import csv

# Function to load data from a CSV file and return it as a list of dictionaries
def load_data(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist
        return []

# Function to save a list of dictionaries to a CSV file
def save_data(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()            # Write column headers
        writer.writerows(data)          # Write all records

# Main menu function
def menu():
    # Load existing records from the CSV file at program start
    chicken_record = load_data("chicken_record.csv")

    while True:
        # Display the menu
        print("\nMain Menu:")
        print("1. Print Chicken List.")
        print("2. Create New Chicken Record.")
        print("3. Update Existing Chicken Record.")
        print("4. Delete An Existing Chicken Record.")
        print("0. Exit.")

        option = input("Enter your choice: ")

        # Exit option
        if option == "0":
            print("Exiting application...")
            break

        # Print all existing chicken records
        elif option == "1":
            print("\nPrinting Chicken List:")
            if chicken_record:
                for index, product in enumerate(chicken_record, start=1):
                    print(f"{index}: {product}")
            else:
                print("No products available.")

#----------------------------------------------------------------------------------------------------------------------

        # Add a new chicken record
        elif option == "2":
            new_name = input("Enter new product name: ")
            chicken_record.append({"name": new_name})  # Add to the in-memory list
            save_data("chicken_record.csv", chicken_record, fieldnames=["name"])  # Save to CSV
            print(f"Product '{new_name}' added successfully!")

#----------------------------------------------------------------------------------------------------------------------

        # Update an existing chicken record
        elif option == "3":
            print("\nUpdating existing chicken:")
            if chicken_record:
                # PRINT chicken names with index value
                for index, record in enumerate(chicken_record, start=1):
                    print(f"{index}: {record['name']}")
                try:
                    # GET user input for chicken index value
                    record_index = int(input("Enter the number of the chicken to update: ")) - 1
                    if 0 <= record_index < len(chicken_record):
                        # GET user input for new chicken name
                        new_name = input("Enter the new name for this chicken: ")
                        confirm = input(f"Confirm update to '{new_name}'? (y/n): ").lower()
                        if confirm == 'y':
                            # UPDATE chicken name at index in chickens list
                            chicken_record[record_index]['name'] = new_name
                            save_data("chicken_record.csv", chicken_record, fieldnames=["name"])
                            print("Chicken record updated successfully!")
                        else:
                            print("Update cancelled.")
                    else:
                        print("Invalid selection. Index out of range.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No chickens available to update.")


#----------------------------------------------------------------------------------------------------------------------

        # Delete a chicken record
        elif option == "4":
            print("\nProduct List:")
            if chicken_record:
                for index, product in enumerate(chicken_record, start=1):
                    print(f"{index}: {product['name']}")
                try:
                    remove_index = int(input("Enter the number of the product to remove: ")) - 1
                    if 0 <= remove_index < len(chicken_record):
                        # Remove the selected record
                        removed_product = chicken_record.pop(remove_index)
                        save_data("chicken_record.csv", chicken_record, fieldnames=["name"])
                        print(f"Product '{removed_product['name']}' removed successfully!")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No products available to delete.")

# Run the menu function
menu()