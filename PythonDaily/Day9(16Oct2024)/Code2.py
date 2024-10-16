# Write a Python program that checks whether a given number is a palindrome (a number that reads the same forwards and backwards). Use loops and conditionals.

def is_palindrome(n):
    str_n = str(n)
    is_palindrome = True
    
    for i in range(len(str_n) // 2):
        if str_n[i] != str_n[-i - 1]:
            is_palindrome = False
            break
    
    return is_palindrome

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")