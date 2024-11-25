"""This task aims to select the shortest typing 
path for the robot through different keyboard 
configurations"""

# Keyboard configurations 
keyboard_1 = \
["abcdefghijklm",
 "nopqrstuvwxyz"]
keyboard_2 = \
["789",
 "456",
 "123",
 "0.-"]
keyboard_3 = \
["chunk",
 "vibex",
 "gymps",
 "fjord",
 "waltz"]
keyboard_4 = \
["bemix",
 "vozhd",
 "grypt",
 "clunk",
 "waqfs"]

#Keyboard Database
keyboard_list = [keyboard_1,keyboard_2,keyboard_3,keyboard_4]

#Initial Data
words = input("Enter a string to type: ")
current_position , current_row = 0,0
final_output = ""

#Movement functions
def move_left(to_move):
    """ This function facilitates movement to the left"""
    return ("l" * abs(to_move)) 

def move_right(to_move):
    """ This function facilitates movement to the right"""
    return ("r" * abs(to_move)) 

def move_up(to_move):
    """ This function facilitates movement upwards"""
    return ("u" * abs(to_move)) 

def move_down(to_move):
    """ This function facilitates movement downwards"""
    return ("d" * abs(to_move))

def keyboard_Check(config_number, string):
    """ This function runs the string through 
    a keyboard and returns the desired path. """

    #Keyboard details and initial data
    chosen_keyboard = keyboard_list[config_number]
    final_output = ""
    current_position, current_row = 0, 0
    
    #Cross referencing each charecter in the string 
    # with the keyboard charecters
    for character in string:
        found = False
        #Runs the charecter check in ever row of the keyboard chosen
        for row in range(len(chosen_keyboard)):
            if character in chosen_keyboard[row]:
                character_position = chosen_keyboard[row].index(character)
                character_row = row
                to_move_horizontal = character_position - current_position
                to_move_vertical = character_row - current_row

                #Path string found
                final_output += check1(to_move_horizontal)+check2(to_move_vertical)+"p"
                
                #Reinitializing basic data for the next charecter
                current_position, current_row = character_position, character_row
                found = True
                break

        #In case of ubknown strings/charecters        
        if not found:
            return False   

    return final_output


def check1(to_move_horizontal):
    """This function facilitates movement
    through a row horizontally and returns 
    horizontal string"""
    output = ""
    if to_move_horizontal < 0:
        output += move_left(to_move_horizontal)
    elif to_move_horizontal >= 0:
        output += move_right(to_move_horizontal)
    return output

def check2(to_move_vertical):
    """This function facilitates movement
    through a column vertically and returns 
    vertical string"""
    output = ""
    if to_move_vertical < 0:
        output += move_up(to_move_vertical)
    elif to_move_vertical > 0:
        output += move_down(to_move_vertical)
    return output

def main(input_string):
    """Main function to facilitate the entire program
    and evaluate the best path for the robot."""
    i = 0

    #All paths from each of the keyboards is appended in the 
    # following list
    final_answers = []
    while i < len(keyboard_list):
        ans = keyboard_Check(i,input_string)
        if ans != False:
            final_answers.append(ans)
        elif ans == False:
            final_answers.append(False)
        i += 1
    
    #Elimination of invalid keyboards for chosen string
    valid_answers = []
    for each in final_answers:
        if each != False:
            valid_answers.append(each)
    if len(valid_answers)==0:
        print("The string cannot be typed out.")
        exit()
    
    #Evaluation of shortest path
    shortest_moves = min(valid_answers, key=len)
    answer_used = final_answers.index(shortest_moves)
    keyboard_used = keyboard_list[int(answer_used)]
    
    #Output
    print("Configuration used:")
    print("-"*(int(len(keyboard_used[0])+4)))
    for k in range(len(keyboard_used)):
        print("| "+keyboard_used[k]+" |")
    print("-"*(int(len(keyboard_used[0])+4)))
    return "The robot must perform the following operations:\n" + shortest_moves

print(main(words))

