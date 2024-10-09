# Write a Python program that counts the number of vowels in a given string.

print("We are going to count number of vowels in the string.")
input_string = input("Enter the String:\n")

vowels = 'aeiouAEIOU'
count = 0
for char in input_string:
    if char in vowels:
        count += 1

print(f"Total numbers of Vowels in String are {count}.")