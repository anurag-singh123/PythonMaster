# Write a Python program to count the number of occurrences of a specific element in a list.

def count_element(lst, element):
    return lst.count(element)

#taking input in the list
my_list = []
while True:
    element = input("Enter an element (or press Enter to finish): ")
    if element == '':
        break
    my_list.append(int(element))
print("Your list is:",my_list)

target = int(input("Enter the target element: "))

# Call the count_element function
count = count_element(my_list, target)

# Print the result
print(f"The element {target} occurs {count} times in the list.")