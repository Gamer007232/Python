import datetime as dt

current_datetime = dt.datetime.now()

print(current_datetime)

string_date = current_datetime.strftime("%A, %d, %B, %Y")
print(string_date)