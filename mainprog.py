from inforep import infofunc #Modules for displaying title, number of amino acids, number of helices, number of sheets and sequence of different chains
from pdbmenu import pdb_menu #print the user menu in terminal window
import histogram as h #Modules to create a histogram representation of all the amino acids present in the protein.
from secstruct import sec_struct#Module for the display of protein secondary structure
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
		#Display to the user the sub menu of options of how they want the histogram to appear 
		print(": H")
		print("Choose an option to order by:")
		print(" "*4,"number of amino acids - ascending (an)")
		print(" "*4,"number of amino acids - descending (dn)")
		print(" "*4,"alphabetically - ascending (aa)")
		print(" "*4,"alphabetically - descending (da)")
		#User provides input based on the options given
		userOption = input(":")
		if userOption == "aa" or "da" or "an" or "dn":
			print("order by:", userOption)
			#Creation of dictionary by calling histo module from histogram.py 
			aadict = h.histo(filename)
			if userOption == "an":
				h.amino_num_ascending(aadict)
			elif userOption == "dn":
				h.amino_num_descending(aadict)
			elif userOption == "aa":
				h.alphabet_ascending(aadict)
			elif userOption == "da":
				h.alphabet_descending(aadict)
		else:
			print("Warning: That input was invalid, please choose aa, da, an or dn next time :-) ")

	elif userInput == "S":
		sec_struct(filename)
		print()
		print()
	elif userInput == "X":
		print("To run function X")

	elif userInput == "Q":
		print("Thank you for analysing with us, ... ByeBye...")
		wlc = False



