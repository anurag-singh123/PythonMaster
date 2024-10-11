# Write a Python program to find the second largest number in a list.

my_list = []
while True:
    element = input("Enter an element (or Press Enter to finish)")
    if element == '':
        break
    my_list.append(int(element))
print("Your list is:",my_list)

my_list.sort(reverse=True)

print("Second largest element in the list is:",my_list[1])