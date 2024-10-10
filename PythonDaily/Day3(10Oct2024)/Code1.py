# Write a Python program to find the greatest common divisor (GCD) of two numbers using loops.

print("We are going to find GCD.\n")
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))

def gcd(a,b):
    i=1
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            gcd=i
        i+=1
    return gcd

print("The GCD of", a, "and", b, "is", gcd(a,b))