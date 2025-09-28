# ask user for a number
a = int(input("Enter a number: "))

# save the original number
temp = a

# variable to store sum of cubes
total = 0

# loop through each digit
while temp > 0:
    digit = temp % 10        # get last digit
    total += digit ** 3      # add cube of digit
    temp //= 10              # remove last digit

# check if equal
if a == total:
    print(a, "is an Armstrong number")
else:
    print(a, "is not an Armstrong number")
