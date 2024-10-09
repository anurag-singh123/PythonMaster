# Write a program to calculate the factorial of a number using a loop.

print("We are going to find factorial of the Number.")
number = int(input("Enter the number:"))

fact = 1
for i in range(1,number+1):
    fact = fact*i

print("Factorial of",number,"is",fact)