# Asking the user to enter a number
number = input("Please enter a number: ")

# Convert the input into a float (to accept decimal numbers too)
number = float(number)

# Now we check the conditions step by step
if number > 0:
    print("The number you entered is positive.")
elif number == 0:
    print("The number you entered is zero.")
else:
    print("The number you entered is negative.")

