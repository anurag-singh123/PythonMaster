# Write a Python program to remove the first and last element from a list using slicing.
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [2, 3, 4]

lst=[]
while True:
    element = input("Enter an element (or press Enter to finish)")
    if element == '':
        break
    lst.append(element)
print("Your list is:",lst)
print(lst[1:len(lst)-1])
