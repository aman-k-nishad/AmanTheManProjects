'''Aim of this program is to help the user put in a code and 
get the variables for the given code'''

import keyword  # We imported the 'keyword' module to check for Python keywords
import re

# This function gets the lines of code from the user in the correct format needed 
def get_user_program():
    user_lines = []  # We create an empty list to store the lines of code
    
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    
    while True:
        line = input()  # Getting the input and remove extra spaces
        if line.lower() == 'end':  
            break
        user_lines.append(line)  # We add the line to our list
    return user_lines  

# This function checks if a word is a valid variable name
def valid_variable(word):
    
    # First, check if the word is empty or doesn't start with a letter or underscore
    if not word or not (word[0].isalpha() or word[0] == '_'):
        return False  # It's not valid, so return False
    
    # Then, we check the rest of the characters in the word
    for char in word[1:]:
        # If any character is not a letter, digit, or underscore, it's not valid
        if not (char.isalnum() or char == '_'):
            return False
    
    # Finally, we check if the word is a Python keyword
    if keyword.iskeyword(word):
        return False  
  
    return True  

# This function extracts and returns the variables from the user's program
def user_variables(user_lines):
    variable_found = set()  # We use a set to store variables and avoid duplicates
    
    # Loop through each line of the user's code
    for line in user_lines:
        words = line.split()  # Split each line into words
        
        # Loop through each word to check if it's a variable
        for word in words:
            # Removing all the non-variable characters like '=', '+', etc.
            correct_word = word.strip('=+*/%:(),')
            # Check if the corrected word is a valid variable
            if valid_variable(correct_word):
                variable_found.add(correct_word)  # Add the valid variable to the set

    return sorted(variable_found)  # Return the variables sorted in alphabetical order

# This function displays the main menu and handles user choices
def display_menu(user_lines):
    while True:
        # Show the main menu to the user
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")  
        print("2. List.")  
        print("0. Quit.")  
        print("==================================")
        
        choice = input().strip()  # Get the user's choice and remove extra spaces

        # If the user chooses '1', print the program
        if choice == '1':
            print("Program:")
            for line in user_lines:  # Loop through and print each line of the program
                print(line)
        
        # If the user chooses '2', list the variables
        elif choice == '2':
            variables = user_variables(user_lines)  # Get the variables from the program
            print("Variables:")
            for variable in variables:  # Print each variable found
                print(variable)
        
        # If the user chooses '0', quit the program
        elif choice == '0':
           break 
        
        # If the user enters an invalid choice, ask them to try again
        else:
            print("Invalid choice, please try again.")

# This is the main function that runs the program
def main():
    user_program = get_user_program()  # Get the program from the user
    display_menu(user_program)  
    
# This ensures the program only runs when executed directly


main()
