from datetime import datetime
import calendar
date = input("Enter a date (DD/MM/YYYY): ")

try:
    datetime.strptime(date, "%d/%m/%Y")
    print(f"{date} is a valid date.")
except ValueError:
    print(f"{date} is not a valid date.")

    y = int(date.split("/")[2])

    if calendar.isleap(y):
        print(f"{y} is a leap year.")  
    else:
        print(f"{y} is not a leap year.")

