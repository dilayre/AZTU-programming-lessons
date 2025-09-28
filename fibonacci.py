# ask the user how many terms
n = int(input("How many terms? "))

# first two numbers
a, b = 0, 1

# check valid input
if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a)
        a, b = b, a + b
