# functions for operations
def add(x, y):        # add two numbers
    return x + y

def subtract(x, y):   # subtract two numbers
    return x - y

def multiply(x, y):   # multiply two numbers
    return x * y

def divide(x, y):     # divide two numbers
    return x / y

print("Select operation:")  # show menu
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# ask user for choice
choice = input("Enter choice (1/2/3/4): ")

# ask user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# check user choice and do calculation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid choice")
