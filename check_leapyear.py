# A year is a leap year if:
# 1. It is divisible by 4
# 2. But not divisible by 100
# 3. Except if it is also divisible by 400

year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(year, "is a leap year.")
elif (year % 100 == 0):
    print(year, "is not a leap year.")
elif (year % 4 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
