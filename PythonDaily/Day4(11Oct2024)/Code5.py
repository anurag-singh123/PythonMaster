# Write a Python program to multiply two matrices (2D lists) and print the resulting matrix.

rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

# Check if the matrices can be multiplied
if cols_A != rows_B:
    print("Error: Matrices cannot be multiplied")
else:
    # Get the elements of matrix A from the user
    A = []
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            row.append(float(input(f"Enter element ({i+1},{j+1}) of matrix A: ")))
        A.append(row)

    # Get the elements of matrix B from the user
    B = []
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            row.append(float(input(f"Enter element ({i+1},{j+1}) of matrix B: ")))
        B.append(row)

    # Multiply the matrices
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or 'range(rows_B)'
                C[i][j] += A[i][k] * B[k][j]

    # Print the resulting matrix
    print("Resulting matrix:")
    for row in C:
        print(" ".join(str(round(x, 2)) for x in row))