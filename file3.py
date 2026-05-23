# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"
print("Please choose one option:-")
print("1) Car")
print("2) Bike")
choice = int(input("\nPlease enter the mode of transport you choose 1 or 2 "))
if choice == 1:
    confirm = input("You chose car. Yes or no? ").lower().strip()[0: 1]
    if confirm == "y":
        print("\nPlease choose the type of car you prefer from the options below:-")
        print("1) Sedan")
        print("2) XUV")
        choice2 = int(
            input("\nPlease enter your preferred choice of car 1 or 2"))
        if choice2 == 1:
            print("Your preferred type of car is sedan. Yes or no?")
        elif choice2 == 2:
            print("Your preferred type of car is XUV")
        else:
            print("!nput €rror")
    elif confirm == "n":
        print("Please choose one option:-")
        print("1) Car")
        print("2) Bike")
        confchoice = int(
            input("\nPlease enter the mode of transport you choose 1 or 2"))
        if confchoice == 1:
            print("You chose car.")
            print("\nPlease choose the type of car you prefer from the options below:-")
            print("1) Sedan")
            print("2) XUV")
            confchoice2 = int(
                input("\nPlease enter your preferred choice of car 1 or 2"))
            if confchoice2 == 1:
                print("Your preferred type of car is sedan. Yes or no?")
            elif confchoice2 == 2:
                print("Your preferred type of car is XUV")
            else:
                print("!nput €rror")
    else:
        print("!nput €rror")
        if confchoice == 2:
            print("\nPlease choose your preferred type of bike from the options below:-")
            print("1) Scooter")
            print("2) Scooty")
            choice3 = int(
                input("Please choose your preferred type of bike from the options below:-"))
            if choice3 == 1:
                print("You have chosen scooter.")
            elif choice3 == 2:
                print("You have chosen scooty")
            else:
                print("!nput €rror")
elif choice == 2:
    confirm2 = input("You chose bike. Yes or no? ").lower().strip()[0: 1]
    if confirm2 == "y":
        print("\nPlease choose your preferred type of bike from the options below:-")
        print("1) Scooter")
        print("2) Scooty")
        choice3 = int(
            input("Please choose your preferred type of bike from the options below:-"))
        if choice3 == 1:
            print("You have chosen scooter.")
        elif choice3 == 2:
            print("You have chosen scooty")
        else:
            print("!nput €rror")
    elif confirm2 == "n":
        print("Please choose one option:-")
        print("1) Car")
        print("2) Bike")
        confichoice = int(
            input("\nPlease enter the mode of transport you choose 1 or 2"))
        if confichoice == 1:
            print("You chose car.")
            print("\nPlease choose the type of car you prefer from the options below:-")
            print("1) Sedan")
            print("2) XUV")
            confichoice2 = int(
                input("\nPlease enter your preferred choice of car 1 or 2"))
            if confichoice2 == 1:
                print("Your preferred type of car is sedan. Yes or no?")
            elif confichoice2 == 2:
                print("Your preferred type of car is XUV")
            else:
                print("!nput €rror")
        elif confichoice == 2:
            print("You have chosen car")
            print("\nPlease choose your preferred type of bike from the options below:-")
            print("1) Scooter")
            print("2) Scooty")
            confichoice3 = int(
                input("Please choose your preferred type of bike from the options below:-"))
            if confichoice3 == 1:
                print("You have chosen scooter.")
            elif confichoice3 == 2:
                print("You have chosen scooty")
            else:
                print("!nput €rror")
    else:
        print("!nput €rror")
else:
    print("!nput €rror")
