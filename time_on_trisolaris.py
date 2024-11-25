""" The user is prompted for and input in seconds 
and it is converted to hours, minutes and leftover seconds.
This is also done for a fictional planet, Trisolaris, for which
the time properties is defined by the user"""


# Collecting input from User
sec_input = int(input("TIME ON EARTH\nInput a time in seconds:"))
# Conversion
hours = sec_input//3600
minutes = (sec_input%3600)//60
seconds = (sec_input%3600)%60
# Output
print("")
print("\nThe time on Earth is", hours,"hours", minutes,"minutes and", seconds, "seconds.")

#Trisolaris
print("\nTIME ON TRISOLARIS")
mins_trisolaris = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
hours_trisolaris = int(input("Input the number of minutes in an hour on Trisolaris:\n"))
#Conversion for Trisolaris
sec_per_hour_trisolaris = mins_trisolaris*hours_trisolaris
total_hours_trisolaris = sec_input//sec_per_hour_trisolaris
sec_remaining_tri = sec_input%sec_per_hour_trisolaris
minutes_trisolaris = sec_remaining_tri//mins_trisolaris
seconds_trisolaris  = sec_remaining_tri%mins_trisolaris
# Output for Trisolaris
print("\nThe time on Trisolaris is", total_hours_trisolaris, "hours", minutes_trisolaris, "minutes and" , seconds_trisolaris , "seconds.")
