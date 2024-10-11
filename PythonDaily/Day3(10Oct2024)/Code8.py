# Write a Python program to sort a dictionary by its values in descending order.

my_dict = {}
n=int(input("Enter the number of key-value pairs:"))

for i in range(n):
    key = input("Enter key {}:".format(i+1))
    value = input("Enter value for {}:".format(key))
    my_dict[key] = value
print("The dictionary is:",my_dict)

sorted_dict = dict(sorted(my_dict.items(),key=lambda item:item[1], reverse=True))

print("The sorted dictionary is:",sorted_dict)