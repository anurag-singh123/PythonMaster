# Write a program to swap the values of two variables without using a temporary variable.

print("We are going swap two variables with each other.")
a = int(input("Enter the first variable"))
b = int(input("Enter the second variable"))
print(f"Before swapping value of A={a} and B={b}")

a = a+b
b = a-b
a = a-b

print(f"After swapping value of A={a} and B={b}")