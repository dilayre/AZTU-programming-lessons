def toBinary(n):
    if n > 1:                 # keep dividing by 2
        toBinary(n // 2)      # recursive call
    print(n % 2, end="")      # print remainder (0 or 1)

# ask user for a number
num = int(input("Enter a number: "))

print("Binary of", num, "is:", end=" ")
toBinary(num)   # call function
print()         # just to move to new line
