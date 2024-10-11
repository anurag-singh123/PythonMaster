# Write a Python program to reverse a list without using the built-in reverse() method.

my_list = []
while True:
    element = input("Enter an element (press Enter to finish): ")
    if element == '':
        break
    my_list.append(element)
print("Your List is:", my_list)

reverse_list = []
for i in range(len(my_list) - 1, -1, -1):
    lst_element = my_list[i]
    reverse_list.append(lst_element)

print("Reversed List is:", reverse_list)