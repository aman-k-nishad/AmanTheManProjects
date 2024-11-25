import copy  # This is used to make deep copies of tables
import tabulate  # This helps display tables in a nice format
import csv  # This is for reading CSV files

# These variables will hold the loaded tables

next_index = 4  # This keeps track of the next available index for adding new tables
deleted_tables = {}  # This will store deleted tables in case we want to restore them later

def loader():
    # This function loads the CSV files into the table variables
    global tables_dict
    
    # Load 'grades.csv' into table_0 and add it to data_tables
    with open('grades.csv', 'r') as zero_csv:
        table_0 = list(csv.reader(zero_csv))  # Convert the CSV data to a list
        data_tables.append(table_0)  # Add it to the list of tables
    
    # Load 'class_students.csv' into table_1
    with open('class_students.csv', 'r') as one_csv:
        table_1 = list(csv.reader(one_csv))
        data_tables.append(table_1)
    
    # Load 'rabbytes_club_students.csv' into table_2
    with open('rabbytes_club_students.csv', 'r') as two_csv:
        table_2 = list(csv.reader(two_csv))
        data_tables.append(table_2)
    
    # Load 'rabbytes_data.csv' into table_3
    with open('rabbytes_data.csv', 'r') as three_csv:
        table_3 = list(csv.reader(three_csv))
        data_tables.append(table_3)

    # Assign each table to the dictionary with its index as the key
    for i in range(len(data_tables)):
        tables_dict[i] = data_tables[i]

# Dictionary to store tables and a list to hold loaded tables
tables_dict = {}
data_tables = []
loader()  # Load the tables from the CSV files

def table_list():
    # This function lists all tables along with the number of columns and rows
    table_listed = [[i, len(tables_dict[i][0]), len(tables_dict[i])] for i in sorted(tables_dict.keys())]  # Get the index, number of columns, and rows for each table
    headers = ["Index", "Columns", "Rows"]  # Table headers
    print(tabulate.tabulate(table_listed, headers, tablefmt="simple"))  # Print the tables in a formatted way
    main() 

def display_table():
    # This function lets the user display a specific table
    try:
        table_choice = input("Choose a table index (to display):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't valid
        display_table() 

    if table_choice not in tables_dict:  # Check if the table index exists
        print("Incorrect table index. Try again.")
        display_table()  

    picked_table = tables_dict[table_choice]  # Get the selected table
    header_row = picked_table[0]  # First row is usually the header
    print(tabulate.tabulate(picked_table[1:], header_row, tablefmt="simple"))  # Print the table
    main()  

def duplicate_table():
    # This function creates a copy of a table
    global next_index  # Use 'global' because we are modifying the next_index variable
    try:
        table_choice = input("Choose a table index (to duplicate):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")  # Show an error if the input isn't valid
        duplicate_table() 

    if table_choice not in tables_dict:  # Check if the table index exists
        print("Incorrect table index. Try again.")
        duplicate_table()  
    
    # Make a deep copy of the table to ensure it's a full independent copy
    picked_table_dup = copy.deepcopy(list(tables_dict[table_choice]))
    
    tables_dict[next_index] = picked_table_dup  # Store the copy in the dictionary at the next available index
    next_index += 1  # Increment the next available index

    main()  # Return to the main menu

def create_table():
    # This function creates a new table by selecting specific columns from an existing table
    global next_index  # Use 'global' to modify next_index
    try:
        table_choice = input("Choose a table index (to create from):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")
        create_table()  

    if table_choice not in tables_dict:  # Check if the table index exists
        print("Incorrect table index. Try again.")
        create_table()  
    
    index_choice = input("Enter the comma-separated indices of the columns to keep:\n")
    indexes = [int(each) for each in index_choice.split(',')]  # Convert the input to a list of integers
    
    new_table = []
    picked = tables_dict[table_choice]  # Get the selected table

    # Loop through each row and pick only the selected columns
    for row in picked:
        new_row = [row[num] for num in indexes]  # Create a new row with the selected columns
        new_table.append(new_row)  # Add the new row to the new table
    
    tables_dict[next_index] = new_table  # Store the new table in the dictionary
    next_index += 1  # Increment the next available index

    main()  =

def delete_table():
    # This function deletes a table
    try:
        table_choice = input("Choose a table index (for table deletion):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")
        delete_table() 

    if table_choice not in tables_dict:  # Check if the table index exists
        print("Incorrect table index. Try again.")
        delete_table()  

    deleted_tables[table_choice] = tables_dict.pop(table_choice)  # Move the deleted table to the backup

    main()  

def delete_column():
    # This function deletes a column from a table
    try:
        table_choice = input("Choose a table index (for column deletion):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")
        delete_column() 

    if table_choice not in tables_dict:  # Check if the table index exists
        print("Incorrect table index. Try again.")
        delete_column()  

    col_choice = input("Enter the index of the column to delete:\n")
    try:
        col_choice = int(col_choice)  # Convert input to an integer
    except ValueError:
        print("Invalid column index. Try again.")
        delete_column()  

    # Loop through the table and remove the selected column from each row
    for row in tables_dict[table_choice]:
        del row[col_choice]

    main()  # Return to the main menu

def restore_table():
    # This function restores a previously deleted table
    try:
        table_choice = input("Choose a table index (for restoration):\n")
        table_choice = int(table_choice)  # Convert input to an integer
    except ValueError:
        print("Incorrect table index. Try again.")
        restore_table() 

    if table_choice in tables_dict or table_choice not in deleted_tables:  # Check if the table can be restored
        print("Incorrect table index. Try again.")
        restore_table()  

    tables_dict[table_choice] = deleted_tables.pop(table_choice)  # Restore the table from the backup

    main()  # Return to the main menu

def main():
    # This is the main menu where the user chooses what to do
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.\n2. Display table.\n3. Duplicate table.\n4. Create table.\n5. Delete table.\n6. Delete column.\n7. Restore table.\n0. Quit.")
    print("==================================")
    choice = input()  # Get the user's choice
    if choice == '1':
        table_list()  # List all tables
    elif choice == '2':
        display_table()  # Display a specific table
    elif choice == '3':
        duplicate_table()  # Duplicate a table
    elif choice == '4':
        create_table()  # Create a new table
    elif choice == '5':
        delete_table()  # Delete a table
    elif choice == '6':
        delete_column()  # Delete a column from a table
    elif choice == '7':
        restore_table()  # Restore a previously deleted table
    elif choice == '0':
        exit()   

main()
