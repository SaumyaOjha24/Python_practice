# Q12 Write a program that takes the name of a month as input and prints the number of days in that
# month. Consider leap years for February.

month = input("Enter month name: ").lower()

if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")

elif month in ["april", "june", "september", "november"]:
    print("30 days")

elif month == "february":
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days (Leap Year)")
    else:
        print("28 days(not a leap year)")

else:
    print("Invalid month name")
