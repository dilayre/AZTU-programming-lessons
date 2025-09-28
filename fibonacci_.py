# function to return Fibonacci number
def recur_fibo(n):
    if n <= 1:       # base case
        return n
    else:            # recursive call
        return recur_fibo(n-1) + recur_fibo(n-2)

# ask user for number of terms
nterms = int(input("How many terms do you want? "))

# check if the number is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
