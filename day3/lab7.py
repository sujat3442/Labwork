#decimal and integer part
a=float(input("Enter a decimal number: "))
b=int(a)
c=b-a
print("Integer part: {}".format(b))
d=abs(c)
print("Decimal part: {}".format(d))