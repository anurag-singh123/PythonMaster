# Write a Python program to find the length of the longest substring in a given string that doesn't have repeating characters.

def longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

s = input("Enter a string: ")
print("Length of the longest substring:", longest_substring(s))