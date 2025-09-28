# ask the user for a number
a = int(input("Enter a number: "))

total = 0

# if number is positive
if a > 0:
    for i in range(1, a + 1):
        total += i

# if number is negative
elif a < 0:
    for i in range(a, 1):   # from num up to 0
        total += i

# if number is zero
else:
    total = 0

print("The sum is", total)
