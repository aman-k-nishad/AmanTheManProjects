"""This task aims to show the navigation of a robot 
while typing out the string provided byb the user accross
a predefined keyboard configuration"""

#Keyboard configuration to be used
keyboard_1 = \
["abcdefghijklm",
 "nopqrstuvwxyz"]

#Initial Data 
words = input("Enter a string to type: ")
current_position = 0
final_output = ""

def move_left(to_move):
    """ This function facilitates movement to the left"""

    global final_output
    final_output += ("l" * abs(to_move))
    return final_output

def move_right(to_move):
    """ This function facilitates movement to the right"""

    global final_output
    final_output += ("r" * abs(to_move)) 
    return final_output


def check(to_move):
    """This function aims to provide the 
    navigatory path of the robot through 
    the above two functions and returns the 
    required robot path string """

    global current_position

    #Decision to move left or right
    if to_move < 0:
        final_output = move_left(to_move)
    else:
        final_output = move_right(to_move)
    current_position += to_move
    return final_output


def keyboard(the_string):
    """This function takes in the input by the user to 
    facilitate the complete movement by calling the apt functions 
    at the time of need""" 

    global final_output
    global current_position

    #Initial row data
    upper_row = True
    lower_row = False

    #Loop to cross reference every chsrecter in the 
    # input string to the keyboards
    for char in the_string:

        # Checking for charecter in the top row
        if char in keyboard_1[0]:
            char_position = keyboard_1[0].index(char)
            to_move = char_position - current_position
            final_output = check(to_move) 
            if lower_row == True:
                final_output += "u"
            final_output += "p"
            upper_row = True
            lower_row = False
        
        # Checking for charecter in the lower row
        elif char in keyboard_1[1]:
            char_position = keyboard_1[1].index(char)
            to_move = char_position - current_position                    
            final_output = check(to_move)
            if upper_row == True:
                final_output += "d"
            final_output += "p"
            upper_row = False
            lower_row = True
    
    # Output
    final_output = "The robot must perform the following operations:\n" + final_output
    for char in the_string:
        if char not in keyboard_1[0] and char not in keyboard_1[1]:
            final_output = "The string cannot be typed out."
    
    return final_output



print(keyboard(words))






