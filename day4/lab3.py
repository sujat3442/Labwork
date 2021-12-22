#job for male or female
g=input("Enter gender (M or F): ")
if g=="F":
    print("Work only in urban areas.")
else:
    a=input("Enter age: ")
    if int(a)>=20 and int(a)<40:
        print("You can work anywhere.")
    elif int(a)>=40 and int(a)<=60:
        print("Work only in urban areas.")
    else:
        print("ERROR")