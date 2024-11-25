'''
This program simulates looting items into containers and multi-containers. It reads item data, container data, and multi-container data from CSV files.
The user can choose a container or multi-container, loot items into them, and list looted items, respecting container capacities.
'''

import csv

# Class to represent a multi-container, which holds multiple containers.
class MultiContainer:
    def __init__(self, name):
        '''
        Initializes a MultiContainer object with a name and sets its weight attributes.
        '''
        self.name = name
        self.empty_weight = 0
        self.current_weight = 0  # Start with zero looted weight.
        self.containers = []  # List of containers inside this multi-container.

    def add_container(self, container):
        '''
        Adds a container to the multi-container and updates its total weight.
        '''
        self.containers.append(container)
        self.empty_weight += container.empty_weight  # Add container's empty weight.
        self.current_weight += container.current_weight  # Add container's current looted weight.

    def loot_item(self, item):
        '''
        Tries to loot an item into one of the multi-container's containers. Returns True if successful.
        '''
        looted = False
        for container in self.containers:  # Try looting in each container.
            if container.loot_item(item):
                looted = True
                self.current_weight += item.weight  # Update multi-container's weight.
                break
        return looted  # Return True if the item was looted.

    def __repr__(self):
        '''
        Returns a string representation of the multi-container, including all its containers and looted items.
        '''
        res = f"{self.name} (total weight: {self.empty_weight + self.current_weight}," + \
              f" empty weight: {self.empty_weight}, capacity: 0/0)"  # Placeholder for capacity.
        for container in self.containers:  # Show each container inside.
            res += '\n   ' + container.alt_str()  # Use container's alternative string representation.
        return res

# Class to represent a single container with a name, empty weight, capacity, and looted items.
class Container:
    def __init__(self, name, empty_weight, capacity):
        '''
        Initializes a Container object with a name, empty weight, and capacity.
        '''
        self.name = name
        self.empty_weight = int(empty_weight)  # Ensure the empty weight is an integer.
        self.capacity = int(capacity)  # Ensure capacity is an integer.
        self.current_weight = 0  # Start with zero looted weight.
        self.items = []  # List to store the looted items.

    def remaining_capacity(self):
        '''
        Calculates and returns the remaining capacity in the container.
        '''
        return self.capacity - self.current_weight

    def loot_item(self, item):
        '''
        Tries to loot an item into the container if it fits within the remaining capacity. Returns True if successful.
        '''
        if self.remaining_capacity() >= item.weight:  # Check if the item can fit.
            self.items.append(item)  # Add item to container.
            self.current_weight += item.weight  # Update current weight.
            return True  # Loot successful.
        return False  # Loot failed due to insufficient capacity.

    def alt_str(self):
        '''
        Returns an alternative string representation of the container, showing looted items in a formatted way.
        '''
        looted_items = "\n      ".join([str(item) for item in self.items])  # Format looted items.
        if looted_items:
            return (f"{self.name} (total weight: {self.empty_weight + self.current_weight}, "
                    f"empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.capacity})\n      {looted_items}")
        else:
            return (f"{self.name} (total weight: {self.empty_weight + self.current_weight}, "
                    f"empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.capacity})")

    def __repr__(self):
        '''
        Returns a string representation of the container, showing its current status and looted items.
        '''
        looted_items = "\n   ".join([str(item) for item in self.items])  # Format looted items.
        if looted_items:
            return (f"{self.name} (total weight: {self.empty_weight + self.current_weight}, "
                    f"empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.capacity})\n   {looted_items}")
        else:
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
        Returns a string representation of the item.
        '''
        return f"{self.name} (weight: {self.weight})"

# Function to read items from a CSV file and return a list of Item objects.
def items_file(user_file):
    '''
    Reads items from a CSV file and returns a list of Item objects.
    '''
    user_items = []
    with open(user_file, mode='r') as f:
        user_reader = csv.reader(f)
        next(user_reader)  # Skip the header row.
        for row in user_reader:
            name, weight = row
            name = name.strip()
            weight = weight.strip()
            if weight.isdigit():  # Check if weight is a valid number.
                user_items.append(Item(name, weight))  # Add item to the list.
    return user_items

# Function to read containers from a CSV file and return a dictionary of Container details.
def containers_file(user_file):
    '''
    Reads containers from a CSV file and returns a dictionary of container details.
    '''
    user_containers = {}
    with open(user_file, mode='r') as f:
        user_reader = csv.reader(f)
        next(user_reader)  # Skip the header row.
        for row in user_reader:
            user_containers[row[0]] = row[1:]  # Store container details in a dictionary.
    return user_containers

# Function to read multi-container data and construct MultiContainer objects.
def multicontainer_file(user_file, user_containers):
    '''
    Reads multi-container data from a CSV file and returns a list of MultiContainer objects.
    '''
    multi_containers = []
    with open(user_file, mode='r') as f:
        user_reader = csv.reader(f)
        next(user_reader)  # Skip the header row.
        for row in user_reader:
            mc = MultiContainer(row[0].strip())  # Create a new MultiContainer.
            for container in row[1:]:  # Add containers to the MultiContainer.
                container = container.strip()
                container = Container(container, user_containers[container][0], user_containers[container][1])
                mc.add_container(container)
            multi_containers.append(mc)  # Add the MultiContainer to the list.
    return multi_containers

# Main function to run the looting program.
def main():
    '''
    Main function that allows the user to loot items into containers or multi-containers.
    '''
    # Read items, containers, and multi-containers from their respective CSV files.
    user_items = items_file('items.csv')
    user_containers = containers_file('containers.csv')
    multi_containers = multicontainer_file('multi_containers.csv', user_containers)

    # Sort items alphabetically by name.
    user_items = sorted(user_items, key=lambda x: x.name)

    # Calculate and print the total number of items and containers.
    total_items = len(user_items) + len(user_containers) + len(multi_containers)
    print(f"Initialised {total_items} items including {len(user_containers) + len(multi_containers)} containers.\n")

    # Ask the user to select a container or multi-container by name.
    selected_container = None
    while not selected_container:
        container_name = input("Enter the name of the container: ")
        found = False
        # Check if the container is a multi-container.
        for container in multi_containers:
            if container.name == container_name:
                selected_container = container
                found = True
                break
        # Check if the container is a regular container.
        for container in user_containers.keys():
            if container == container_name:
                selected_container = Container(container, user_containers[container][0], user_containers[container][1])
                found = True
                break
        if not found:
            print(f'"{container_name}" not found. Try again.\n')

    # Main loop to show the menu and handle user choices.
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Loot item.")  # Option to loot an item into the selected container.
        print("2. List looted items.")  # Option to display looted items.
        print("0. Quit.")  # Option to quit the program.
        print("==================================")
        choice = input().strip()

        if choice == '1':
            # Loot item.
            while True:
                item_name = input("Enter the name of the item: ").strip()
                item_to_loot = next((item for item in user_items if item.name == item_name), None)

                if item_to_loot:  # Check if item exists.
                    if selected_container.loot_item(item_to_loot):  # Try looting the item.
                        print(f'Success! Item "{item_name}" stored in container "{selected_container.name}".')
                    else:
                        print(f'Failure! Item "{item_name}" NOT stored in container "{selected_container.name}".')
                    break  # Exit the loop after looting.
                else:
                    print(f'"{item_name}" not found. Try again.\n')

        elif choice == '2':
            # List looted items.
            print(selected_container)  # Display the selected container with looted items.

        elif choice == '0':
            # Quit the program.
            break

        else:
            # Handle invalid input.
            print(f"\n==================================")
            print("Invalid choice. Please enter 1, 2, or 0.")
            print(f"==================================\n")

# Entry point of the program.
main()

