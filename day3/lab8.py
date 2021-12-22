#sum of digits in number
a=int(input("Enter a number: "))

b=0
for digit in str(a):
    b+=int(digit)
print(b)