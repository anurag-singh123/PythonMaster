# Write a Python program to check if a given list is already sorted in ascending order or descending order.

#taking input int the list
my_list = []
while True:
    element = input("Enter an element (or press Enter to finish)")
    if element == "":
        break
    my_list.append(int(element))

asorted_list = sorted(my_list)
if(asorted_list == my_list):
    print(my_list,"This list is sorted in ascending order.")
else:
    print(my_list,"This list is not sorted in ascending order.")

dsorted_list = sorted(my_list, reverse=True)
if(dsorted_list == my_list):
    print(my_list,"This list is sorted in descending order.")
else:
    print(my_list,"This list is not sorted in descending order.")