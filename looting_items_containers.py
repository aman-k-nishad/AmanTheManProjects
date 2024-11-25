'''
This program reads two CSV files: one containing item details and the other containing container details.
It allows the user to loot items into containers based on available capacity, and displays looted items or container details as needed.
'''

import csv

# Class to represent containers with their name, empty weight, capacity, and looted items.
class Container:
    def __init__(self, name, empty_weight, capacity):
        '''
        Initializes a Container object with a name, empty weight, capacity, and sets current looted weight to 0.
        '''
        self.name = name
        self.empty_weight = int(empty_weight)  # Ensure the empty weight is an integer.
        self.capacity = int(capacity)  # Ensure capacity is an integer.
        self.current_weight = 0  # Start with zero looted weight.
        self.items = []  # List to store the looted items.

    def remaining_capacity(self):
        '''
        Returns the remaining capacity of the container after looting.
        '''
        return self.capacity - self.current_weight

    def loot_item(self, item):
        '''
        Attempts to loot an item into the container. Returns True if successful, False if it exceeds capacity.
        '''
        if self.remaining_capacity() >= item.weight:  # Check if item fits in remaining capacity.
            self.items.append(item)  # Add item to container.
            self.current_weight += item.weight  # Update current weight.
            return True  # Loot successful.
        return False  # Loot failed due to insufficient capacity.

    def __repr__(self):
        '''
        Returns a string representation of the container's details, including looted items.
        '''
        looted_items = "\n   ".join([str(item) for item in self.items])  # Format looted items.
        if looted_items:  # If items were looted, show them.
            return (f"{self.name} (total weight: {self.empty_weight + self.current_weight}, "
                    f"empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.capacity})\n   {looted_items}")
        else:  # No items looted, show container details only.
            return (f"{self.name} (total weight: {self.empty_weight + self.current_weight}, "
                    f"empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.capacity})")

# Class to represent items with a name and weight.
class Item:
    def __init__(self, name, weight):
        '''
        Initializes an Item object with a name and weight.
        '''
        self.name = name
        self.weight = int(weight)  # Ensure the weight is an integer.

    def __repr__(self):
        '''
        Returns a string representation of the item's details.
        '''
        return f"{self.name} (weight: {self.weight})"

# Function to read items from a CSV file and return a list of Item objects.
def items_file(user_file):
    '''
    Reads items from a CSV file and returns a list of Item objects.
    '''
    user_items = []  # List to store items.
    with open(user_file, mode='r') as file:
        user_reader = csv.reader(file)
        next(user_reader)  # Skip the header row.
        for row in user_reader:  # Process each row.
            name, weight = row  # Extract name and weight.
            name = name.strip()  # Remove any extra spaces from the name.
            weight = weight.strip()  # Remove any extra spaces from the weight.
            if weight.isdigit():  # Ensure the weight is a valid number.
                user_items.append(Item(name, weight))  # Create an Item and add it to the list.
    return user_items  # Return the list of items.

# Function to read containers from a CSV file and return a list of Container objects.
def containers_file(user_file):
    '''
    Reads containers from a CSV file and returns a list of Container objects.
    '''
    user_containers = []  # List to store containers.
    with open(user_file, mode='r') as file:
        user_reader = csv.reader(file)
        next(user_reader)  # Skip the header row.
        for row in user_reader:  # Process each row.
            name, empty_weight, capacity = row  # Extract name, empty weight, and capacity.
            name = name.strip()  # Remove any extra spaces from the name.
            empty_weight = empty_weight.strip()  # Remove any extra spaces from the empty weight.
            capacity = capacity.strip()  # Remove any extra spaces from the capacity.
            if empty_weight.isdigit() and capacity.isdigit():  # Ensure both are valid numbers.
                user_containers.append(Container(name, empty_weight, capacity))  # Create a Container and add it to the list.
    return user_containers  # Return the list of containers.

# Main function to run the looting program.
def main():
    '''
    Main function that reads item and container data, allows user to loot items, and displays looted items or container details.
    '''
    # Read items and containers from respective CSV files.
    user_items = items_file('items.csv')
    user_containers = containers_file('containers.csv')

    # Sort items and containers alphabetically by name.
    user_items = sorted(user_items, key=lambda x: x.name)  # Sort items by name.
    user_containers = sorted(user_containers, key=lambda x: x.name)  # Sort containers by name.

    # Calculate and print the total number of items and containers.
    total_items = len(user_items) + len(user_containers)  # Total count.
    print(f"Initialised {total_items} items including {len(user_containers)} containers.\n")

    # Ask the user to select a container by name.
    selected_container = None
    while not selected_container:
        container_name = input("Enter the name of the container: ").strip()  # Prompt user for container name.
        for container in user_containers:  # Search for the selected container.
            if container.name == container_name:
                selected_container = container  # Select the container if found.
                break
        if not selected_container:  # If not found, prompt again.
            print(f'"{container_name}" not found. Try again.\n')

    # Main loop to handle user choices.
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Loot item.")  # Option to loot an item.
        print("2. List looted items.")  # Option to display looted items.
        print("0. Quit.")  # Option to quit the program.
        print("==================================")
        choice = input().strip()  # Get user's choice.

        if choice == '1':
            # Loot item option.
            while True:
                item_name = input("Enter the name of the item: ").strip()  # Prompt for item name.
                item_to_loot = next((item for item in user_items if item.name == item_name), None)  # Find item.

                if item_to_loot:  # If item is found.
                    if selected_container.loot_item(item_to_loot):  # Attempt to loot the item.
                        print(f'Success! Item "{item_name}" stored in container "{selected_container.name}".')
                    else:  # If item cannot be looted due to lack of capacity.
                        print(f'Failure! Item "{item_name}" NOT stored in container "{selected_container.name}".')
                    break  # Exit after attempt.
                else:
                    print(f'"{item_name}" not found. Try again.\n')  # If item not found, prompt again.

        elif choice == '2':
            # List looted items option.
            print(selected_container)  # Display container with looted items.

        elif choice == '0':
            # Quit the program.
            break  # Exit the loop and quit.

        else:
            # Handle invalid input.
            print("\n==================================")
            print("Invalid choice. Please enter 1, 2, or 0.")  # Prompt for valid input.
            print("==================================\n")

# Entry point of the program.
main()

