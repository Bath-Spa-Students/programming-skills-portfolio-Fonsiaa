#using a module function
import datetime #access a code
current_time=datetime.datetime.now() #showing the current time
formatted_time=current_time.strftime("%D-%M-%Y %H-%M-%S")
print("Current Date and Time:",formatted_time) #prints the date and time
