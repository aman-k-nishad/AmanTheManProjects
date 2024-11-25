'''Aim of this program is to help the user put in a code and 
get the variables formatted to snake case  for the given code'''


import keyword  # We imported the 'keyword' module to check for Python keywords
import re

# Function to get the lines of code from the user
def get_user_program():
    user_lines = []  # We create an empty list to store the lines of code
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    
    # We use a loop to collect lines of code from the user
    while True:
        line = input()  # We get the user's input for a line of code
        if line.lower() == 'end':  # If the user types 'end', we stop taking input
            break
        user_lines.append(line)  # We add the line of code to our list
    return user_lines  # We return all the lines of code the user provided

# Function to check if a word is a valid variable name
def valid_variable(word):
    # First, we check if the word starts with a letter or underscore
    if not word or not (word[0].isalpha() or word[0] == '_'):
        return False  # If not, it's not a valid variable name
    
    # Next, we loop through the remaining characters in the word
    for char in word[1:]:
        # If any character is not a letter, digit, or underscore, it's not valid
        if not (char.isalnum() or char == '_'):
            return False
    
    # We also need to check if the word is a Python keyword (like 'if', 'for', etc.)
    if keyword.iskeyword(word):
        return False  # If it is a keyword, it's not valid as a variable name
    
    return True  # If all checks pass, we return True to indicate it's a valid variable name

# Function to extract and return variables from the user's program
def user_variables(user_lines):
    variable_found = set()  # We create an empty set to store unique variables
    
    for line in user_lines:
        words = line.split()  
        
        for word in words:
            # We remove characters like '=', '+', etc., that are not part of the variable
            correct_word = word.strip('=+*/%:(),')
            
            # We check if the cleaned word is a valid variable name
            if valid_variable(correct_word):
                variable_found.add(correct_word)  # If it's valid, we add it to the set
    
    return sorted(variable_found) 

# Function to convert a given variable to snake_case
def snake(variable):
    snake_case = ""  # We start with an empty string to build the snake_case name
    index = 0  
    
    # We use a while loop to go through each character in the variable name
    while index < len(variable):
        char = variable[index]  # We get the current character
        
        if char.isupper():
            if index != 0:
                snake_case += "_"  # We add an underscore before the lowercase letter
            snake_case += char.lower()  # We convert the character to lowercase and add it
        else:
            snake_case += char  # If it's not uppercase, we just add the character as is
        
        index += 1  # We move to the next character
    return snake_case  # We return the snake_case version of the variable

# Function to replace a variable with its snake_case equivalent in the program
def format_variable_to_snake(user_lines, variable):
    snake_case_variable = snake(variable)  # Convert the variable to snake_case
    formatted_lines = []  # List to store the formatted lines

    for line in user_lines:
        # Use re.split to split the line into words but keep the spaces intact
        words_and_spaces = re.split(r'(\W+)', line)  # Split by non-word characters but retain them
        
        new_line = ""  # String to build the new formatted line
        
        # Loop through the parts of the line (words and spaces)
        for part in words_and_spaces:
            # Check if the part matches the variable (ignoring surrounding characters)
            if part.strip('=+*/%:(),') == variable:
                # If it matches, replace it with the snake_case version
                new_line += part.replace(variable, snake_case_variable)
            else:
                new_line += part  # If it doesn't match, leave it unchanged
        
        formatted_lines.append(new_line)  # Add the newly formatted line to the list
    
    return formatted_lines  # Return the formatted lines

# Main menu function
def display_menu(user_lines):
       while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")  # Option to print the whole program
        print("2. List.")  # Option to list all the variables found
        print("3. Format.")  # Option to format a variable to snake_case
        print("0. Quit.")  # Option to quit the program
        print("==================================")
        
        choice = input().strip()  # We get the user's choice and remove extra spaces

        if choice == '1':  
            print("Program:")
            for line in user_lines:  # We loop through and print each line of the program
                print(line)
        
        elif choice == '2':  
            variables = user_variables(user_lines)  
            print("Variables:")
            for variable in variables:  
                print(variable)
        
        elif choice == '3':  
            variables = user_variables(user_lines)  
            if not variables: 
                print("No variables found to format.")
                continue  
            while True:
                print("Pick a variable:")
                selected_variable = input().strip()  
                
                if selected_variable in variables:  # If the selected variable exists in the list
                    user_lines = format_variable_to_snake(user_lines, selected_variable)
                    break  # After formatting, we return to the main menu
                else:
                    print(f"This is not a variable name.")  # If the variable is not valid, show an error

        elif choice == '0': 
            break  # Exit the loop and end the program
        
        else:
            print("Invalid choice, please try again.") 

# Main function to run the program
def main():
    user_program = get_user_program() 
    display_menu(user_program)  # We display the menu for user interaction

main()
