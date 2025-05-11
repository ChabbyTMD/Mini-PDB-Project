from pdb_analyzer import PDBAnalyzer
import os

def print_menu(current_file="None"):
    """Display the main menu"""
    width = 66  # Total width of the menu
    border = '*' * width
    
    # Menu items with their corresponding keys
    menu_items = [
        ("1) Open a PDB File", "O"),
        ("2) Information", "I"),
        ("3) Show histogram of amino acids", "H"),
        ("4) Display Secondary Structure", "S"),
        ("5) Exit", "Q")
    ]
    
    print(border)
    print(f"{'* PDB FILE ANALYSER':*^{width}}*")
    print(border)
    print(f"* {'Select an option below:':<{width-4}} *")
    print(f"*{' ':^{width-2}}*")
    
    # Print menu items with consistent spacing
    for item, key in menu_items:
        # Calculate padding to align all items
        padding = width - len(item) - len(key) - 7  # 7 accounts for the '* ' and ' ()', '*' chars
        print(f"* {item}{' ' * padding}({key}) *")
    
    print(f"*{' ':^{width-2}}*")
    print(f"* {'Current PDB: ' + str(current_file):<{width-4}} *")
    print(border)

def main():
    analyzer = None
    wlc = True
    wlc_0 = True
    
    print_menu()
    userInput = input("Welcome, Enter option O or Q: ").upper()
    
    while wlc_0:
        if userInput == "O":
            filename = input("Please enter a valid file name: ")
            if not os.path.exists(filename):
                print("(((WARNING)))")
                print("The file does not exist")
                continue
            
            # Validate if it's a proper PDB file
            is_valid, error_message = PDBAnalyzer.is_valid_pdb_file(filename)
            if not is_valid:
                print("(((WARNING)))")
                print(f"Invalid PDB file: {error_message}")
                continue
                
            print("Valid PDB file detected, loading...")
            analyzer = PDBAnalyzer(filename)
            wlc_0 = False
        elif userInput == "Q":
            wlc_0 = False
            wlc = False
        else:
            print("Please enter a valid option")
            userInput = input("Enter option O, Q: ").upper()

    while wlc:
        print_menu(analyzer.filename if analyzer else "None")
        userInput = input("Enter another option O, I, H, S, X, Q: ").upper()
        
        if userInput == "I":
            analyzer.get_info()
            print("\n")
            
        elif userInput == "O":
            fn = True
            while fn:
                filename = input("Enter a new filename: ")
                if not os.path.exists(filename):
                    print("(((WARNING)))")
                    print("The file does not exist")
                    continue
                    
                # Validate if it's a proper PDB file
                is_valid, error_message = PDBAnalyzer.is_valid_pdb_file(filename)
                if not is_valid:
                    print("(((WARNING)))")
                    print(f"Invalid PDB file: {error_message}")
                    continue
                    
                print("**********Valid PDB file detected**********")
                analyzer.load_file(filename)
                print("\n")
                fn = False

        elif userInput == "H":
            print(": H")
            print("Choose an option to order by:")
            print(" " * 4, "number of amino acids - ascending (an)")
            print(" " * 4, "number of amino acids - descending (dn)")
            print(" " * 4, "alphabetically - ascending (aa)")
            print(" " * 4, "alphabetically - descending (da)")
            
            sort_option = input(":").lower()
            if sort_option in ["aa", "da", "an", "dn"]:
                print("order by:", sort_option)
                analyzer.get_histogram(sort_option)
            else:
                print("Warning: That input was invalid, please choose aa, da, an or dn next time :-) ")

        elif userInput == "S":
            analyzer.get_secondary_structure()
            print("\n")

        elif userInput == "Q":
            print("Thank you for analysing with us, ... ByeBye...")
            wlc = False

if __name__ == "__main__":
    main()
