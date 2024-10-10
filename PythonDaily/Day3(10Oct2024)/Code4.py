# Write a Python program to find the transpose of a matrix (2D list).
import numpy as np

rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns"))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

print("The input matrix is:")
for row in matrix:
    print(row)

transpose_matrix = np.transpose(matrix)
print("The transpose of matrix is:")
print(transpose_matrix)