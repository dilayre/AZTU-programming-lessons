# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221, 872]

# use anonymous function to filter numbers divisible by 7
result = list(filter(lambda x: (x % 7 == 0), my_list))

# display the result
print("Numbers divisible by 7 are", result)
