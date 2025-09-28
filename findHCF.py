# ask the user to enter two numbers
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))

# choose the smaller number first
if no1 > no2:
    smaller = no2
else:
    smaller = no1

# check which number divides both
for i in range(1, smaller + 1):
    if (no1 % i == 0) and (no2 % i == 0):
        hcf = i   # keep updating "Highest Common Factor" when condition is true

# print the result
print("The HCF of", no1, "and", no2, "is:", hcf)

