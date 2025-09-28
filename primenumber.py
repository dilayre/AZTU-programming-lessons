# take input from the user
num = int(input("Enter a number: "))

# numbers less than 2 are not prime
if num < 2:
    print(num, "is not prime")
else:
    # assume the number is prime
    prime = True

    # check all numbers from 2 to num-1
    for i in range(2, num):
        # if num is divisible by i, it is not prime
        if num % i == 0:
            prime = False
            break

    # print the result
    if prime:
        print(num, "is prime")
    else:
        print(num, "is not prime")
