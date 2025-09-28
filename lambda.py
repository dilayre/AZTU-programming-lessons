# ask the user for number of terms
terms = int(input("How many terms? "))

print("The total terms are:", terms)

# loop to calculate powers of 2
for i in range(terms):
    value = 2 ** i      # calculate power
    print("2 raised to power", i, "is", value)
