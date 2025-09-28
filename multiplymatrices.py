# enter first 3x3 matrix
print("Enter first matrix (3x3), row by row:")
X = []
for i in range(3):
    row = list(map(int, input("Row " + str(i+1) + ": ").split()))
    X.append(row)

# enter second 3x4 matrix
print("Enter second matrix (3x4), row by row:")
Y = []
for i in range(3):
    row = list(map(int, input("Row " + str(i+1) + ": ").split()))
    Y.append(row)

# make result 3x4 with zeros
result = [[0]*4 for _ in range(3)]

# multiply matrices
for i in range(3):          # rows of X
    for j in range(4):      # cols of Y
        for k in range(3):  # elements to multiply
            result[i][j] += X[i][k] * Y[k][j]

# print final matrix
print("Result:")
for row in result:
    print(row)
