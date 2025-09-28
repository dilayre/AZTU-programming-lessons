# function to calculate sum
def recur_sum(n):
    if n <= 1:              # base case: if n is 1 or 0
        return n
    else:                   # recursive case
        return n + recur_sum(n - 1)

# ask user for a number
number = int(input("Enter a positive number: "))

# check if the number is valid
if number < 0:
    print("Please enter a positive number")
else:
    print("The sum of natural numbers up to", number, "is:", recur_sum(number))
