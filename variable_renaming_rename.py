import keyword
import re

def get_user_program():
    user_lines = []
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    
    while True:
        line = input()
        if line.lower() == 'end':
            break
        user_lines.append(line)
    return user_lines

def valid_variable(word):
    if not word or not (word[0].isalpha() or word[0] == '_'):
        return False
    for char in word[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    if keyword.iskeyword(word):
        return False
    return True

def user_variables(user_lines):
    variable_found = set()
    for line in user_lines:
        words = line.split()
        for word in words:
            correct_word = word.strip('=+*/%:(),')
            if valid_variable(correct_word):
                variable_found.add(correct_word)
    return sorted(variable_found)

def snake(variable):
    snake_case = ""
    index = 0
    while index < len(variable):
        char = variable[index]
        if char.isupper():
            if index != 0:
                snake_case += "_"
            snake_case += char.lower()
        else:
            snake_case += char
        index += 1
    return snake_case

def format_variable_to_snake(user_lines, variable):
    snake_case_variable = snake(variable)
    formatted_lines = []

    for line in user_lines:
        words_and_spaces = re.split(r'(\W+)', line)
        new_line = ""
        for part in words_and_spaces:
            if part.strip('=+*/%:(),') == variable:
                new_line += part.replace(variable, snake_case_variable)
            else:
                new_line += part
        formatted_lines.append(new_line)
    
    return formatted_lines

def rename(user_lines):
    variables = user_variables(user_lines)
    while True:
        print("Pick a variable:")
        variable_selected = input().strip()
        if variable_selected in variables:
            while True:
                print("Pick a new variable name:")
                new_variable_name = input().strip()
                if not valid_variable(new_variable_name):
                    print("Invalid variable name. Please try again.")
                elif new_variable_name in variables:
                    print("This is already a variable name.")
                else:
                    for i in range(len(user_lines)):
                        user_lines[i] = re.sub(r'\b{}\b'.format(variable_selected), new_variable_name, user_lines[i])
                    return user_lines
        else:
            print("This is not a variable name.")

def display_menu(user_lines):
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("4. Rename.")
        print("0. Quit.")
        print("==================================")
        
        choice = input().strip()

        if choice == '1':
            print("Program:")
            for line in user_lines:
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
                
                if selected_variable in variables:
                    user_lines = format_variable_to_snake(user_lines, selected_variable)
                    break
                else:
                    print("This is not a variable name.")
        
        elif choice == '4':
            user_lines = rename(user_lines)
        
        elif choice == '0':
            break
        
        else:
            print("Invalid choice, please try again.")

def main():
    user_program = get_user_program()
    display_menu(user_program)

main()
