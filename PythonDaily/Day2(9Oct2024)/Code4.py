# Write a Python program to find the sum of all the elements in a list.

my_list = [int(x) for x in input("Enter a list of numbers seprated by spaces:").split()]

sum=0
for i in my_list:
    sum += i

print(f"Sum of List is {sum}")