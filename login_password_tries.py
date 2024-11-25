"""This task aims to create a login program 
which requires user name and password to e correct"""

#User names and passwords are srtored in a list for cross referencing with the input
name_list = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password_list = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","apple","11111","hello","admin"]
condition = False

#Trials left
tries=3

#The following loop runs 3 times before it breaks 
# thereby giving user three tries at logging in
while condition == False:
    tries-=1
    if tries<0:
        break
    username = input("Enter username: ")
    password = input("Enter password: ")

    #Cross-referencing
    if username in name_list:
        if password in password_list:
            print("Login successful. Welcome" , username , "!")
            condition = True
            break
        elif password not in password_list:
            print("Login incorrect. Tries left:", tries)

    # Breaking of loop on exhausting the three tries
    elif tries<0:
        print("Login incorrect. Tries left:", tries)        
        break
        
    # Loops to next trial
    elif username not in name_list:
        print("Login incorrect. Tries left:", tries)
        

    
