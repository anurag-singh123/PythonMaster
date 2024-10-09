# Write a Python program that takes a list of numbers and sorts them in ascending order.

my_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
print("Original List:",my_list)

my_list = sorted(my_list)

print("Sorted List:",my_list)