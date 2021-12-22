#smallest in 3 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a<b and a<c:
    print("{} is smallest".format(a))
elif b<a and b<c:
    print("{} is smallest".format(b))
elif c<a and c<b:
    print("{} is smallest".format(c))
else:
    print("Some or all numbers might be equal, please enter different numbers")