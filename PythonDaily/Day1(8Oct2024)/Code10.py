# Write a Python program to check if a given string is a palindrome or not.

print("We are going to check string is palindrome or not")
my_string = input("Enter the String:\n")
reversed_string = my_string[::-1]

if reversed_string == my_string:
    print("String is Palindrome")
else:
    print("String is not Palindrome")