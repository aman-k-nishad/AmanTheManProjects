'''
This program reads two CSV files: one containing item information and the other containing container information.
It processes the data, sorts items and containers alphabetically, and prints the total number of both, along with their details.
'''

import csv

# Class to represent containers with their name, empty weight, and capacity.
class Container:
    def __init__(self, name, empty_weight, capacity):
        '''
        Initializes a Container object with a name, empty weight, and capacity.
        '''
        self.name = name
        self.empty_weight = int(empty_weight)  # Ensure empty weight is an integer.
        self.capacity = int(capacity)  # Ensure capacity is an integer.
        self.initial = 0  # Initial value set to zero.
    
    def __repr__(self):
        '''
        Returns a string representation of the container's details.
        '''
        return f"{self.name} (total weight: {self.empty_weight}, empty weight: {self.empty_weight}, capacity: {self.initial}/{self.capacity})"

# Class to represent items with their name and weight.
class Item:
    def __init__(self, name, weight):
        '''
        Initializes an Item object with a name and weight.
        '''
        self.name = name
        self.weight = int(weight)  # Ensure weight is an integer.

    def __repr__(self):
        '''
        Returns a string representation of the item's details.
        '''
        return f"{self.name} (weight: {self.weight})"

# Function to read item details from a CSV file.
def items_file(user_file):
    '''
    Reads items from a CSV file and returns a list of Item objects.
    '''
    user_items = []  # List to store item objects.
    with open(user_file, mode='r') as file: 
        user_reader = csv.reader(file)  
        next(user_reader)  # Skip the header row.
        for row in user_reader:  # Process each row of the file.
            name, weight = row  # Extract item name and weight.
            name = name.strip()  # Remove extra spaces in the name.
            weight = weight.strip()  # Remove extra spaces in the weight.
            if weight.isdigit():  # Ensure weight is a valid number.
                user_items.append(Item(name, weight))  # Add item to the list.
    return user_items  # Return the list of items.

# Function to read container details from a CSV file.
def containers_file(user_file):
    '''
    Reads containers from a CSV file and returns a list of Container objects.
    '''
    user_containers = []  # List to store container objects.
    with open(user_file, mode='r') as file: 
        user_reader = csv.reader(file)  
        next(user_reader)  # Skip the header row.
        for row in user_reader:  # Process each row of the file.
            name, empty_weight, capacity = row  # Extract container details.
            name = name.strip()  # Remove extra spaces in the name.
            empty_weight = empty_weight.strip()  # Remove extra spaces in empty weight.
            capacity = capacity.strip()  # Remove extra spaces in capacity.
            if empty_weight.isdigit() and capacity.isdigit():  # Ensure both weights are valid numbers.
                user_containers.append(Container(name, empty_weight, capacity))  # Add container to the list.
    return user_containers  # Return the list of containers.

# Main function to process and display the data.
def main():
    '''
    Reads items and containers from CSV files, sorts them, and displays the total count and details.
    '''
    # Read items and containers from respective CSV files.
    user_items = items_file('items.csv') 
    user_containers = containers_file('containers.csv')  

    # Sort both items and containers alphabetically by their name.
    user_items = sorted(user_items, key=lambda x: x.name)  # Sort items.
    user_containers = sorted(user_containers, key=lambda x: x.name)  # Sort containers.

    # Calculate and print the total number of items and containers.
    total_items = len(user_items) + len(user_containers) 
    print(f"Initialized {total_items} items including {len(user_containers)} containers.\n") 

    # Print all items in the sorted order.
    print("Items:")
    for item in user_items:  # Loop through each item and print details.
        print(item)
    
    # Print all containers in the sorted order.
    print("\nContainers:")
    for container in user_containers:  # Loop through each container and print details.
        print(container)

    # Placeholder for further functionality, left intentionally blank.
    print()

# Entry point of the program.
main()

