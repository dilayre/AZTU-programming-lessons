# take numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# assume first number is the biggest
big = a

if b > big:
    big = b

if c > big:
    big = c

print("Largest number is:", big)
