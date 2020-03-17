def infofunc(namefile):
    """This function accepts the filename entered by the user and displays The title of the protein, the number of helices, sheets, amino acids as well as the string of amino acids for each protein chain"""
    with open(namefile, 'r') as myfile:   #The context manager needs to be updated to accept file name input by the user. probably as a global variable. 
        whole_file = myfile.readlines()
        #some empty lists, strings and dictionaries
        helix_dictionary = {}
        sheet_dictionary = {}
        aminoacidcount_dictionary = {}
        amino_string = {}
        seqres_list = []
        whole_seq_string_1 = ""
        chainnum_string = ""
        title_string = ""

        #some empty lists and dictionaries
        aminocodes = dict(ALA = "A", ARG= "R", ASN="N", ASP="D", ASX="B", CYS="C", GLU="E", GLN="Q", GLX="Z", GLY="G", HIS="H", ILE="I", LEU="L", LYS="K", MET="M", PHE="F", PRO="P", SER="S", THR="T", TRP="W", TYR="Y", VAL="V")
        for i in range(len(whole_file)):
            #Loop through all the elements in whole file list as string records...
            seqres = whole_file[i]
            #This next section checks an empty dictionary if the chain identifier is present. 
            #If not it adds the chain identifier as a new key and gives a value of 1. 
            #When subsequent identifiers are found it will assign the correct number of amino acids listed in the PDB file column 14 to 17
            if seqres.startswith("TITLE"):
                title_string += seqres[10:] 
            if seqres.startswith("SEQRES"):
                if seqres[11] in aminoacidcount_dictionary: 
                    seqres_list_clean = []
                    aminoacidcount_dictionary[seqres[11]] = int(seqres[13:19])#Heavily redundant since the number at [14:17] is the same for all records matching the same chain ID.

                elif seqres[11] not in aminoacidcount_dictionary:
                    aminoacidcount_dictionary[seqres[11]] = int(seqres[13:19])
                    
                        
                #Amino acid code conversions.     
                if seqres[11] not in amino_string:
                    seqres_list = seqres.split(" ") #Place string words into new list
                    seqres_list_clean = [bb for bb in seqres_list[5:] if bb != '' and bb != '\n']#Remove empty string elements and new line characters from the list and placing them in a new list seqres_list_clean
                    seqres_complete = []
                    seqres_complete.extend(seqres_list_clean[1:])# Create and empty list seqres_complete and extend it with only amino acids. NOTE index[0] of seqres_list_clean contains the amino acid number 167. So add items starting from index 1.
                    whole_seq_string = ""
                    for s in range(len(seqres_complete)):
                        whole_seq_string += aminocodes[seqres_complete[s]]
                               
                elif seqres[11] in amino_string:
                    seqres_list = seqres.split(" ") #Place string words into new list
                    seqres_list_clean = [aa for aa in seqres_list[5:] if aa != '' and aa != '\n']
                    seqres_complete = []
                    seqres_complete.extend(seqres_list_clean[1:])# Create and empty list seqres_complete and extend it with only amino acids. NOTE index[0] of seqres_list_clean contains the amino acid number 167. So add items starting from index 1.
                    for sq in range(len(seqres_complete)):
                        whole_seq_string += aminocodes[seqres_complete[sq]]
                   
                amino_string[seqres[11]] = whole_seq_string
                
            #The next section starts with an empty dictionary and adds the helix chain identifier as a new key in a dictionary and assigns the value 1 to it
            #Next when the same identifier is found in subsequent records it will increment the value associated with the helix chain identifier key by 1
            
            if seqres.startswith("HELIX"):
                if seqres[19:20] in helix_dictionary:
                    helix_dictionary[seqres[19:20]] += 1
                elif seqres[19:20] not in helix_dictionary:
                    helix_dictionary[seqres[19:20]] = 1
                    
            #NOTE: Same logic as the helix section above...
            
            if seqres.startswith("SHEET"):
                if seqres[32:33] in sheet_dictionary:
                    sheet_dictionary[seqres[32:33]] += 1
                elif seqres[32:33] not in sheet_dictionary:
                    sheet_dictionary[seqres[32:33]] = 1

    print("Title: ", title_string) #Print the title of the PDB file

    chainnum_string = aminoacidcount_dictionary.keys()

    chainnum_string_1 = " and ".join(chainnum_string)

    print("CHAINS: ", chainnum_string_1) #Print the Chain ID's of the various chains of the protein.
    
    for x,y in aminoacidcount_dictionary.items():
        print("--Chain", x)
        print("Number of amino acids :", y)
        try:
            print("Number of helix :",7*" ", helix_dictionary[x])
        except KeyError:
            print("Number of helix :",7*" ","0")
        try:
            print("Number of sheet :",7*" ", sheet_dictionary[x])
        except KeyError:
            print("Number of sheet :",7*" ","0")#When a particular chain does not have a sheet, 0 is displayed 
        rep = amino_string[x]
        a = 0
        print("Sequence:")
        for i in range(int(len(amino_string[x])/50) + 1):# Get the length of the string and divide it by 50(Number of amino acids to display) This results in 3 complete sets of 50 plus 1 remainder.
            b = a + 50
            print(18*" ", rep[a:b])#String slicing starting from a as 0 and b as 50, then a as 50 and b as 100, then a as 100 then b as 150, then the rest is printed
            a += 50
    return None

                    

