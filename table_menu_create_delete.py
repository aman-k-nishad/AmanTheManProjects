

import copy
import tabulate
import csv

# These variables will store the tables from the CSV files

next_index = 4  # This keeps track of the next index to use when adding new tables

def loader():
    # This function loads the data from CSV files into our tables
    global tables_dict  # We use 'global' to make sure we modify the global variables
    
    # Open and read the CSV file for 'grades.csv'
    with open('grades.csv', 'r') as zero_csv:
        table_0 = list(csv.reader(zero_csv))  # Convert the CSV data to a list and store it in table_0
        data_tables.append(table_0)  # Add this table to our main data_tables list
    
    # Same as above but for 'class_students.csv'
    with open('class_students.csv', 'r') as one_csv:
        table_1 = list(csv.reader(one_csv))
        data_tables.append(table_1)
    
    # Now, load 'rabbytes_club_students.csv'
    with open('rabbytes_club_students.csv', 'r') as two_csv:
        table_2 = list(csv.reader(two_csv))
        data_tables.append(table_2)
    
    # And finally, load 'rabbytes_data.csv'
    with open('rabbytes_data.csv', 'r') as three_csv:
        table_3 = list(csv.reader(three_csv))
        data_tables.append(table_3)

    # We add each table to our dictionary using its index as the key
    for i in range(len(data_tables)):
        tables_dict[i] = data_tables[i]

# This dictionary will store all our tables, using their indices as keys
tables_dict = {}
data_tables = []
loader()  # Call the function to load the tables from the CSV files


def table_list():
    # This function shows a list of all the tables, along with the number of columns and rows they have
    table_listed = [[i, len(tables_dict[i][0]), len(tables_dict[i])] for i in tables_dict]  # For each table, get its index, column count, and row count
    headers = ["Index", "Columns", "Rows"]  # These are the table headers
    print(tabulate.tabulate(table_listed, headers, tablefmt="simple"))  # Print the list of tables in a nice format
    main() 

def display_table():
    # This function lets the user pick a table to display its contents
    try:
        table_choice = input("Choose a table index (to display):\n")
        table_choice = int(table_choice)  # Convert the input to an integer (since indices are numbers)
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't a number
        display_table()  

    if table_choice not in tables_dict:  # Check if the chosen index is valid
        print("Incorrect table index. Try again.")
        display_table()  

    picked_table = tables_dict[table_choice]  # Get the chosen table from the dictionary
    header_row = picked_table[0]  # The first row is usually the header (column names)
    print(tabulate.tabulate(picked_table[1:], header_row, tablefmt="simple"))  # Print the rest of the table, nicely formatted
    main()  

def duplicate_table():
    # This function creates a copy of an existing table
    global next_index  # We use 'global' because we're updating the next_index variable
    try:
        table_choice = input("Choose a table index (to duplicate):\n")
        table_choice = int(table_choice)
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't a valid number
        duplicate_table()  

    if table_choice not in tables_dict:  # Check if the chosen index is valid
        print("Incorrect table index. Try again.")
        duplicate_table()  
    
    # Make a deep copy of the table (deepcopy makes sure it's a full, independent copy)
    picked_table_dup = copy.deepcopy(list(tables_dict[table_choice]))
    
    tables_dict[next_index] = picked_table_dup  # Add the duplicated table to the dictionary with a new index
    next_index += 1  # Increase the next available index

    main() 

def create_table():
    # This function creates a new table by picking certain columns from an existing one
    global next_index  # We use 'global' because we're updating the next_index variable
    try:
        table_choice = input("Choose a table index (to create from):\n")
        table_choice = int(table_choice)  # Convert input to integer
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't valid
        create_table() 

    if table_choice not in tables_dict:  # Check if the chosen index is valid
        print("Incorrect table index. Try again.")
        create_table() 
    
    index_choice = input("Enter the comma-separated indices of the columns to keep:\n")
    index_intm = index_choice.split(',')  # Split the input into individual column indices
    indexes = [int(each) for each in index_intm]  # Convert each index to an integer
    
    new_table = []
    picked = tables_dict[table_choice]  # Get the chosen table

    # Loop through each row in the table and pick only the selected columns
    for row in picked:
        new_row = [row[num] for num in indexes]  # Create a new row with just the chosen columns
        new_table.append(new_row)  # Add the new row to the new table
    
    tables_dict[next_index] = new_table  # Add the new table to the dictionary at the next available index
    next_index += 1  # Increment the index counter

    main()  
    

def delete_table():
    # This function deletes a table from the dictionary
    try:
        table_choice = input("Choose a table index (for table deletion):\n")
        table_choice = int(table_choice)  # Convert input to integer
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't valid
        delete_table()  

    if table_choice not in tables_dict:  # Check if the chosen index is valid
        print("Incorrect table index. Try again.")
        delete_table()  # Try again

    del tables_dict[table_choice]  # Remove the table from the dictionary

    main()  # Go back to the main menu
    

def main():
    # This is the main menu where the user chooses what to do
    global data_tables  # Use global to access the data_tables list
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.\n2. Display table.\n3. Duplicate table.\n4. Create table.\n5. Delete table.\n0. Quit.")  # Show options
    print("==================================")
    choice = input()  
    if choice == '1':
        table_list() 
    elif choice == '2':
        display_table()  
    elif choice == '3':
        duplicate_table()  
    elif choice == '4':
        create_table()  
    elif choice == '5':
        delete_table()  
    elif choice == '0':
        exit()  # Quit the program

main()  # Call the main function to start the program
