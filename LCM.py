# ask the user to enter two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# choose the bigger number first
if a > b:
    greater = a
else:
    greater = b

# keep checking until we find a common multiple
while True:
    if (greater % a == 0) and (greater % b == 0):
        lcm = greater   # found the LCM
        break           # stop the loop
    greater += 1        # try the next number

# show the result
print("The LCM of", a, "and", b, "is:", lcm)
