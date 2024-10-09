# Write a Python program to check whether a number is prime or not.


def PrimeNumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True



print("We are going to find number is Prime or not.")
n = int(input("Enter the Number:"))

if PrimeNumber(n):
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime Number")