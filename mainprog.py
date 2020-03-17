from inforep import infofunc
from pdbmenu import pdb_menu
import os
pdb_menu()
wlc = True
wlc_0 = True#while loop condition (wlc)...
userInput = input("Welcome, Enter option O or Q")
userInput = userInput.upper() #To convert the input character into upper case
while wlc_0 is True:
    if userInput == "O":
        filename = input("Please enter a valid file name")
        if os.path.exists(filename):
            wlc_0 = False
        else:
            print("(((WARNING)))")
            print("The above file does not exist")
            pass
    elif userInput == "Q":
        wlc_0 = False
        wlc = False
    else:
        print("Please enter a valid option")
        userInput = input("Enter option O, Q")
        userInput = userInput.upper()

while wlc is True:
    pdb_menu(filename)
    userInput = input("Enter another option O, I, H, S, X, Q")
    userInput = userInput.upper()
    
    if userInput == "I":
        infofunc(filename)
        print()
        print()
        
    elif userInput == "O":
        fn = True
        while fn is True:
            filename = input("Enter a new filename")
            if os.path.exists(filename):
                print("**********Valid file name**********")
                print()
                print()
                fn = False
            else:
                print("(((WARNING)))")
                print("Invalid filename entered.")
    elif userInput == "H":
        print("To run function H")
    elif userInput == "S":
        print("To run function S")
    elif userInput == "X":
        print("To run function X")

    elif userInput == "Q":
        print("Thank you for analysing with us, ... ByeBye...")
        wlc = False



