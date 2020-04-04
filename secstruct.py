def sec_struct(namefile):    
    '''
        Accept a valid PDB filename and display a representation of the secondary structure of the protein i.e. Sheets and Helices
    '''
    with open(namefile, 'r') as myfile:    
        whole_file_list = myfile.readlines()
        sheet_dict = {}
        helix_dict = {}
        chain_dict = {}
        representation_dict = {}
        #Initialize dictionaries to keep the positions of the sheet and helix of the representation.i.e sheet and helix dictionaries 
        #Initialize dictionary to keep a record of how many residues each chain has i.e. chain_dict
        #Initialize dictionary to keep a initial representation of each chain with '-' characters.
        for i in range(len(whole_file_list)):
            whole_file_record = whole_file_list[i]
            if whole_file_record.startswith("SHEET"): #Create a dictionary whose key is the sheet feature tag name and the value is the sheet range of the feature within the chain.
                sheet_dict.update({whole_file_record[8:10] + whole_file_record[12:14]:(whole_file_record[21],int(whole_file_record[23:26]),int(whole_file_record[34:37]))}) #(key-sheet-tag : value(ChainID, Start_residue/position, End_residue/position))
            
            if whole_file_record.startswith("HELIX"):
                helix_dict.update({whole_file_record[12:14]:(whole_file_record[19],int(whole_file_record[21:25]), int(whole_file_record[34:37]))})#(key-Helix_tag : value-(ChainID, Start_residue/position, End_residue/position))
        
            if whole_file_record.startswith("SEQRES"):
                chain_dict.setdefault(whole_file_record[11:12],int(whole_file_record[13:18]))#(key-ChainID, value-number_of_amino_acid_residues)
                
        for key, value in chain_dict.items():
            representation_dict.update({key:list(value*"-")})


    for k in sheet_dict.values():
        replist=representation_dict[k[0]] #k[0] is the ChainID item in the sheet_dict.values() tuple.
        del replist[k[1]:k[2]+1] #manipulate the representation dict list-representation by deleting the specific number of elements specified in the sheet_dict values tuple i.e k[1]-start-position, k[2]-end position. k[2]+1 is required to delete the last required element.
        for l in range(k[2] - k[1]+1):
            replist.insert(k[1]-1,'|')
            representation_dict.update({k[0]:replist}) #k[0] refers to the Chain-ID which is the appropriate key in the representation_dict.
            
    for k in helix_dict.values():
        replist=representation_dict[k[0]]
        del replist[k[1]:k[2]+1]
        for l in range(k[2] - k[1]+1):
            replist.insert(k[1]-1,'/')
            representation_dict.update({k[0]:replist})
            
    print("Secondary structure of the PDB id:", namefile)
    for key,value in representation_dict.items():
        print("Chain:",key)
        final_representation=''.join(representation_dict[key])
        start = 0
        for counter in range(int(len(final_representation)/80+1)): #Display the final representation but to limit the number of characters to 80.
            end = start + 80
            print(final_representation[start:end])
            start += 80
        print(len(final_representation))
