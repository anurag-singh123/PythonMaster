#Write a program to count the number of alphabets and numbers of digits in the string 'Nagpur-440010'

my_string='Nagpur-440010'

alphabet_count=0
digit_count=0
for char in my_string:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1

print("Alaphabets:",alphabet_count)
print("Digits:",digit_count)