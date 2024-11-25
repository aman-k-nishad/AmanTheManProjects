"""This task aims to create a login program"""


# Using the names, a list is made to cross check the input with
name_list = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
condition = False

#Loop works until correct input is provided and matched with in the list.
while condition == False:
    username = input("Enter username: ")
    if username in name_list:
        print("Login successful. Welcome" , username , "!")
        condition = True
        break
    else:
        print("Login incorrect.")
