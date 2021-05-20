import datetime as dt

date_string = "21 June, 2021"

date_object = dt.datetime.strptime(date_string, "%d %B, %Y")

print("date object:", date_object)