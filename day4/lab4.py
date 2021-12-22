#absolute value
#using abs function
a=int(input("Enter a number: "))
b=abs(a)
print("Absolute value using abs function: ",b)

#using maths
if a<0:
    b=a*(-1)
    print("Absolute value using maths: ",b)
else:
    print("Absolute value using maths: ",a)

#using for loop
print("Absolute value using for loop:", end=" ")
for i in str(a):
    if i=="-":
        continue
    print(i,end="")
print(" ")

#using while loop
print("Absolute value using while loop:", end=" ")
j=0
while j<len(str(a)):
    if str(a)[j]=="-":
        j+=1
        continue
    else:
        print(str(a)[j],end="")
        j+=1