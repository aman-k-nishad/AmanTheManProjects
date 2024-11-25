"""This program uses the logic from task 1 and task 2 and additionally
prompts the user to give some seconds which can be added to the existing
time in trisolaris"""


# Collecting input from User
sec_input = int(input("TIME ON EARTH\nInput a time in seconds:"))

# Conversion to seconds
hours = sec_input//3600
minutes = (sec_input%3600)//60
seconds = (sec_input%3600)%60

# Output
print("")
print("\nThe time on Earth is", hours,"hours", minutes,"minutes and", seconds, "seconds.")

# Trisolaris
print("\nTIME ON TRISOLARIS")
mins_trisolaris = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
hours_trisolaris = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

# Conversion for Trisolaris
sec_per_hour_trisolaris = mins_trisolaris*hours_trisolaris
total_hours_trisolaris = sec_input//sec_per_hour_trisolaris
sec_remaining_tri = sec_input%sec_per_hour_trisolaris
total_minutes_trisolaris = sec_remaining_tri//mins_trisolaris
total_seconds_trisolaris  = sec_remaining_tri%mins_trisolaris

# Output for Trisolaris
print("\nThe time on Trisolaris is", total_hours_trisolaris, "hours", total_minutes_trisolaris, "minutes and" , total_seconds_trisolaris , "seconds.")


#Addition of time for seconds_trisolaris

print("\nTIME AFTER WAITING ON TRISOLARIS")
waiting_period = int(input("Input a duration in seconds:\n"))
#Conversion
hours_waited = waiting_period//sec_per_hour_trisolaris
seconds_remaining_after_waiting = waiting_period%sec_per_hour_trisolaris
minutes_waited = seconds_remaining_after_waiting//mins_trisolaris
seconds_waited = seconds_remaining_after_waiting%mins_trisolaris

#Addition
post_wait_hour_trisolaris = total_hours_trisolaris+hours_waited
post_wait_minutes_trisolaris = total_minutes_trisolaris+minutes_waited
post_wait_seconds_trisolaris = total_seconds_trisolaris+seconds_waited

if post_wait_minutes_trisolaris >= hours_trisolaris or post_wait_seconds_trisolaris >= mins_trisolaris:
    post_wait_minutes_trisolaris += post_wait_seconds_trisolaris // mins_trisolaris
    post_wait_seconds_trisolaris = post_wait_seconds_trisolaris % mins_trisolaris
    post_wait_hour_trisolaris += post_wait_minutes_trisolaris // hours_trisolaris
    post_wait_minutes_trisolaris = post_wait_minutes_trisolaris % hours_trisolaris

final_hour_trisolaris = post_wait_hour_trisolaris
final_minutes_trisolaris = post_wait_minutes_trisolaris
final_seconds_trisolaris = post_wait_seconds_trisolaris
#Output
print("\nThe time on Trisolaris after waiting is", final_hour_trisolaris, "hours", final_minutes_trisolaris, "minutes and", final_seconds_trisolaris, "seconds.")



