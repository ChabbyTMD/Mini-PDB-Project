def histo(namefile):
    """Function keeps count of every amino acid occurance in the pdb file and returns a ditionary of the final values."""
    amino_acid_dictionary = {"ALA":0, "ARG":0, "ASN":0, "ASP":0, "ASX":0, "CYS":0, "GLU":0, "GLN":0, "GLX":0, "GLY":0, "HIS":0, "ILE":0, "LEU":0, "LYS":0, "MET":0, "PHE":0, "PRO":0, "SER":0, "THR":0, "TRP":0, "TYR":0, "VAL":0}
    with open(namefile, 'r') as myfile:    
        whole_file_list = myfile.readlines()
        seq_string_a = ""
        for i in range(len(whole_file_list)):
            whole_file_record = whole_file_list[i]
            if whole_file_record.startswith("SEQRES"):
                seq_string = whole_file_record[17:70]
                seq_string_a = seq_string_a + seq_string
        new_seq = seq_string_a.split(' ')
        new_seq_clean = []

        for liny in range(len(new_seq)):#loop through the string of amino acids to remove '' and \n and populate the list new_seq_clean with ONLY amino acids
            if new_seq[liny] != '':
                new_seq_clean.append(new_seq[liny])


        for amino_acid_a in range(len(new_seq_clean)):
            amino_acid_dictionary[new_seq_clean[amino_acid_a]] += 1 ##Iterate through the dictionary to count and record every occurance of each amino acid
    
    return amino_acid_dictionary

def alphabet_ascending(amino_acid_dictionary):
    """To accept a dictionary containing the number of each amino acid and print a representation of the number of amino acids in alphabetically ascending order"""
    for elem in sorted(amino_acid_dictionary.items()):
        if elem[1]>0: #to exclude non-existent amino acids in the final histogram
            print(elem[0] , " :" , "*"*elem[1])
            
def alphabet_descending(amino_acid_dictionary):
    """This accepts a dictionary containing the number of each amino acid and prints a representation of each amino acid in descending alphabetical order"""
    for elem in sorted(amino_acid_dictionary.items(), reverse=True): #reverse sorts the keys in descending order
        if elem[1]>0: #to exclude non-existent amino acids in the final histogram
            print(elem[0] , " :" , "*"*elem[1])
            
def amino_num_ascending(amino_acid_dictionary):
    """ This accepts a dictionary containing the number of each amino acid and prints a representation of amino acids in ascending order according to number"""
    # Create a list of tuples sorted by index 1 i.e. value field. The key function returns the 1th index of the tuple which is the number of each amino acid   
    listofTuples = sorted(amino_acid_dictionary.items() ,  key=lambda x: x[1])

    # Iterate over the sorted sequence
    for elem in listofTuples :
        if elem[1]>0:
            print(elem[0] , " :" , "*"*elem[1])
    
def amino_num_descending(amino_acid_dictionary):
    """ This accepts a dictionary containing the number of each amino acid and prints a representation of amino acids in descending order according to number """
    # Create a list of tuples sorted by index 1 i.e. value field     
    listofTuples = sorted(amino_acid_dictionary.items() ,reverse=True,  key=lambda x: x[1])

    # Iterate over the sorted sequence
    for elem in listofTuples :
        if elem[1]>0:
            print(elem[0] ,  " :" ,"*"*elem[1])
    