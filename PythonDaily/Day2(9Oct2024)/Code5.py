# Write a Python program to find the largest number in a list provided by the user.

my_list = [int(x) for x in input("Enter a list of numbers seprated by spaces:").split()]
largest_number=max(my_list)
print(f"Largest Number in {my_list} is {largest_number}")