# Write a Python program to count the number of vowels and consonants in a string entered by the user. Use a loop to iterate over the characters and conditionals to classify them as vowels or consonants.

# Get the input string from the user
user_input = input("Enter a string: ")

# Initialize counters for vowels and consonants
vowels = 0
consonants = 0

# Loop over each character in the input string
for char in user_input:
    # Convert the character to lowercase to make the check case-insensitive
    char = char.lower()
    
    # Check if the character is a vowel
    if char in 'aeiou':
        vowels += 1
    # Check if the character is a consonant (i.e., not a vowel and not a space)
    elif char.isalpha() and char not in 'aeiou':
        consonants += 1

# Print the results
print("Vowels:", vowels)
print("Consonants:", consonants)