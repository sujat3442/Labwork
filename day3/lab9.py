#username and password
for i in range(0,3):
    a=input("Enter username: ")
    b=input("Enter password: ")
    if a=="abc" and b=="123":
        print("Logged in successfully")
        break
    else:
        print("Incorrect username or password")
else:
        print("Attempts finished")
