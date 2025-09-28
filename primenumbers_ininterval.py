# take input from the user (you can change the values)
lower = int(input("starting number: "))
upper = int(input("ending number: "))

print("Prime numbers between", lower, "and", upper, "are:")

# go through all numbers in the interval
for num in range(lower, upper + 1):

    # numbers less than 2 are not prime
    if num < 2:
        continue

    # assume the number is prime
    prime = True

    # check for factors
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    # if prime is still True, print the number
    if prime:
        print(num)
