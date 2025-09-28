import calendar   # import calendar module

# ask the user for year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# print the calendar of that month
print("\nHere is the calendar:")
print(calendar.month(year, month))
