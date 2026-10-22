from datetime import datetime
import calendar
date = input("Enter a date (DD/MM/YYYY): ")

try:
    datetime.strptime(date, "%d/%m/%Y")
    print(f"{date} is a valid date.")

    year = int(date.split("/")[2])

    if calendar.isleap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print(f"{date} is not a valid date.")