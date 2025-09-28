# Equation: ax² + bx + c = 0

# Get numbers from user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Find discriminant (d = b² - 4ac)
d = b**2 - 4*a*c

if d > 0:
    # Two different real answers
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print("Two roots:", x1, "and", x2)
elif d == 0:
    # One answer
    x = -b / (2*a)
    print("One root:", x)
else:
    # No real answer
    print("No real roots")

