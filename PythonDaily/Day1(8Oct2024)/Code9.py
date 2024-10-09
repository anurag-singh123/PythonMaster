# Write a Python program to display the Fibonacci sequence up to a certain number of terms, taken from the user.

print("We are going to print Fibonacci Series to the given number")
num = int(input("Enter the number"))

first,second = 0,1

for i in range(0,num-1):
    last=first+second
    first=second
    second=last

print(f"Fibonacci Series of {num} is {last}")