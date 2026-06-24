ask = input("Do u have a medical cause? (Y/N):").strip().upper()
if ask == "Y":
    print("You are allowed.")
else:
    attendance = int(input("What is the attendance (percentage) of the student?"))
    if attendance >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")