# original matrix (3 rows, 2 columns)
X = [[12, 7],
     [4, 5],
     [3, 8]]

# empty matrix for result (2 rows, 3 columns)
result = [[0, 0, 0],
          [0, 0, 0]]

# go through rows and columns
for i in range(3):          # 3 rows in X
    for j in range(2):      # 2 columns in X
        result[j][i] = X[i][j]   # swap rows and columns

# print final matrix
print("Transpose:")
for row in result:
    print(row)
