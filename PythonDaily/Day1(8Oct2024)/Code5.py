# Write a program to find the maximum of three numbers entered by the user.

print("We are going to find max number among three.")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if(a>b and a>c):
    print(a,"is Greater Number")
elif(b>a and b>c):
    print(b,"is Greater Number")
else:
    print(c,"is Greater Number")

