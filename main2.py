print("Select ride:")
print("1.Bike")
print("2.Car")

choice = int(input("Enter ur choice."))

if choice == 1:
    print("What type of bike?")
    print("1.Scooty")
    print("2.Scooter")
    choice2 = int(input("Enter ur type of bike pls"))
    if choice2 == 1:
        print("U have selected scooty.")
    else:
        print("U have selcted scooter.")
elif choice == 2:
    print("What type of car?")
    print("1.Sedan")
    print("2.XUV")
    choice2 = int(input("Enter ur type of car pls"))
    if choice2 == 1:
        print("U have selected Sedan.")
    else:
        print("U have selected XUV.")


