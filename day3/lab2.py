#result
maths=float(input("Enter marks in maths: "))
sci=float(input("Enter marks in science: "))
com=float(input("Enter marks in computer: "))
eng=float(input("Enter marks in english: "))
total=maths+sci+com+eng
if total>400:
    print("Enter valid marks")
else:
    print("Total: {}".format(total))
    per=total/4
    print("Percentage: {}%".format(per))
    print("Result:", end=" ")
    if per>=70:
        print("Distinction")
    elif per>=60 and per<70:
        print("First division")
    elif per>=40 and per<60:
        print("Pass")
    else:
        print("Fail")