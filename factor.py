# ask the user to enter a number
x = int(input("Enter a number: "))

# show message
print("The factors of", x, "are:")

# check all numbers from 1 to num
for i in range(1, x + 1):
    if x % i == 0:   # if divisible, then it's a factor
        print(i)
