"""The task aims to create a login program similar to 
task 5 but with an additional providion 
to check if the user is a robot or not"""


#Username and their respective passwords
user1 = ['Ava', '12345']
user2 = ['Leo', 'abcde']
user3 = ['Raj', 'pass1']
user4 = ['Zoe', 'qwert']
user5 = ['Max', 'aaaaa']
user6 = ['Sam', 'zzzzz']
user7 = ['Eli', '11111']
user8 = ['Mia', 'apple']
user9 = ['Ian', 'hello']
user10 = ['Kim', 'admin']

#This list of the usernames and their respective passwords for cross referencing
user_list = [user1,user2,user3,user4,user5,user6,user7,user8,user9,user10]
try_left = 3

#Loop to cross check the input with the pairs of usernames 
# and passwords in the database list
while try_left > 0:
    login = False
    # User Inputs
    username = input("Enter username: ")
    password = input("Enter password: ")

    #Cross-checking
    for element in user_list:
        if username == element[0]:
            if password == element[1]:
                print("Login successful. Welcome", username, "!")
                login = True
                break
    if login == True:
        break
    try_left -= 1
    print("Login incorrect. Tries left:", try_left)
    
    #Loop to deal with the robot checks as soon as trials allowed are over.
    j=3
    while try_left <= 0:
        robotest = input("Are you a robot (Y/n)? ")
        if robotest.lower() == "y" or robotest == "":
            break
        elif robotest == "n":
            try_left = 3
            break
        j-=1
        #Loop breaks on exhausting robot check trials
        if j <= 0:
            break

    


