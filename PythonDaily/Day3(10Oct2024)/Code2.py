# Write a Python program to generate a list of squares of numbers from 1 to 10 using list comprehension.

my_list = []
while True:
    element = input("Enter an element (or press Enter to finish): ")
    if element == "":
        break
    my_list.append(int(element))

squared_list = [i**2 for i in my_list]

print("The input list is:", my_list)
print("The list of squares is:",squared_list)