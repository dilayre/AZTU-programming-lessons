# two 3x3 matrices
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# empty matrix for the result
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# go through rows one by one
for i in range(3):          # 3 rows
    for j in range(3):      # 3 columns
        result[i][j] = X[i][j] + Y[i][j]   # add elements

# print the final matrix
print("Result:")
for row in result:
    print(row)
