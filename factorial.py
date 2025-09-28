# recursive function
def factorial(n):
    # base case: stop when n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # recursive step: n * factorial of (n-1)
    return n * factorial(n - 1)

# take number from user
a = int(input("Enter a number: "))

# negative numbers are not allowed
if a < 0:
    print("factorial is not defined for negative numbers")
else:
    print("The factorial of", a, "is", factorial(a))
