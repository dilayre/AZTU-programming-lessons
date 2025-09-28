# Ask the user for a number
number = int(input("Enter a number: "))

if number % 2 == 0:
    # If remainder is 0, it means the number is even
    result = "even"
else:
    # Otherwise, the number is odd
    result = "odd"

# Show the final result in one clear line
print("The number", number, "is", result)
