#sum of three different integers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a!=b and a!=c and b!=c:
    sum=a+b+c
    print("Sum: ",sum)
else:
    print("0")