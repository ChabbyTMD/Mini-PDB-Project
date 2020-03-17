def aminocounter(namefile):
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