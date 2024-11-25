""" The user is prompted for and input in seconds 
and it is converted to hours, minutes and leftover seconds"""

# Collecting input from User
sec_input = int(input("TIME ON EARTH\nInput a time in seconds:"))
# Conversion
hours = sec_input//3600
minutes = (sec_input%3600)//60
seconds = (sec_input%3600)%60
# Output
print("")
print("\nThe time on Earth is", hours,"hours", minutes,"minutes and", seconds, "seconds.")



