import datetime
current_time=datetime.datetime.now()
formatted_time=current_time.strftime("%D-%M-%Y %H-%M-%S")
print("Current Date and Time:",formatted_time)