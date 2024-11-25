import copy
import tabulate
import csv

def loader():
    """
    This function loads the CSV files into data tables.
    It reads four different CSV files and stores each as a list of rows in a global list 'data_tables'.
    """
    global data_tables

    # Open and read the 'grades.csv' file, store its contents as a table (list of rows).
    with open('grades.csv', 'r') as zero_csv:
        table_0 = list(csv.reader(zero_csv))  # Convert the CSV file to a list of rows
        data_tables.append(table_0)  # Add the table to the data_tables list
    
    # Open and read the 'class_students.csv' file
    with open('class_students.csv', 'r') as one_csv:
        table_1 = list(csv.reader(one_csv))
        data_tables.append(table_1)
    
    # Open and read the 'rabbytes_club_students.csv' file
    with open('rabbytes_club_students.csv', 'r') as two_csv:
        table_2 = list(csv.reader(two_csv))
        data_tables.append(table_2)
    
    # Open and read the 'rabbytes_data.csv' file
    with open('rabbytes_data.csv', 'r') as three_csv:
        table_3 = list(csv.reader(three_csv))
        data_tables.append(table_3)

# Create an empty list to store all data tables
data_tables = []
loader()

def table_list(data_received):
    """
    This function prints a list of all loaded tables, including the number of columns and rows in each table.
    """
    # Create a list of tables with their index, number of columns, and rows
    table_listed = [[i, len(data_tables[i][0]), len(data_tables[i])] for i in range(len(data_tables))]
    
    # Define the headers for the table list
    headers = ["Index", "Columns", "Rows"]
    
    # Print the table list in a neat format using 'tabulate'
    print(tabulate.tabulate(table_listed, headers, tablefmt="simple"))
    
    # Return to the main menu
    main()

def display_table(tables_data):
    """
    This function displays the content of a selected table.
    It asks the user to input the table index, checks if it's valid, and then prints the selected table.
    """
    try:
        # Ask the user for a table index and convert it to an integer
        table_choice = input("Choose a table index (to display):\n")
        table_choice = int(table_choice)
    except ValueError:
        # If the input is not a valid number, show an error message and retry
        print("Incorrect table index. Try again.")
        display_table(data_tables)

    # Check if the table index is within the valid range
    if table_choice not in range(0, len(tables_data)):
        print("Incorrect table index. Try again.")
        display_table(data_tables)

    # Get the table the user selected
    picked_table = tables_data[table_choice]
    
    # Extract the first row as the header
    header_row = picked_table[0]
    
    # Print the table (excluding the header) using 'tabulate'
    print(tabulate.tabulate(picked_table[1:], header_row, tablefmt="simple"))
    
    # Return to the main menu
    main()

def duplicate_table(table_data):
    """
    This function duplicates a selected table and adds it to the data tables list.
    """
    try:
        # Ask the user for the table index to duplicate
        table_choice = input("Choose a table index (to duplicate):\n")
        table_choice = int(table_choice)
    except ValueError:
        # If the input is invalid, show an error message and retry
        print("Incorrect table index. Try again.")
        duplicate_table(data_tables)

    # Check if the table index is valid
    if table_choice not in range(0, len(data_tables)):
        print("Incorrect table index. Try again.")
        duplicate_table(data_tables)
    
    # Make a deep copy of the selected table (to ensure changes to the original table don't affect the copy)
    picked_table_dup = copy.deepcopy(list(data_tables[table_choice]))

    # Add the duplicated table to the data_tables list
    data_tables.append(picked_table_dup)
    
    # Return to the main menu
    main()

def main():
    """
    Main function that displays the menu and handles user choices.
    The user can list tables, display a table, duplicate a table, or quit the program.
    """
    global data_tables  # Access the global list of data tables
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.\n2. Display table.\n3. Duplicate table.\n0. Quit.")
    print("==================================")
    
    # Get the user's choice
    choice = input()
    
    # Perform the action based on the user's input
    if choice == '1':
        table_list(data_tables)  # List all tables
    elif choice == '2':
        display_table(data_tables)  # Display a table
    elif choice == '3':
        duplicate_table(data_tables)  # Duplicate a table
    elif choice == '0':
        exit()  # Quit the program

# Start the program by calling the main function
main()
