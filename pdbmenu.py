def pdb_menu(filename="None"):
    """Function to print out menu to terminal window. filename is the name of the valid pdb file loaded in memory."""
    """When ran for the first time filename will be displayed as None"""
    
    print('*'*66)
    print('* PDB FILE ANALYSER  %45s'%'*')
    print('*'*66)
    print('* Select an option below: %40s'%'*')
    print('* %64s'%'*')
    print('* %30s'%' 1) Open a PDB FIle %29s'%'(O) %13s'%'*')
    print('* %26s'%' 2) Information %33s'%'(I) %13s'%'*')
    print('* %44s'%' 3) Show histogram of amino acids %15s'%'(H) %13s'%'*')
    print('* %42s'%' 4) Display Secondary Structure %17s'%'(S) %13s'%'*')
    print('* %30s'%' 5) Export PDB File %29s'%'(X) %13s'%'*')
    print('* %19s'%' 6) Exit %40s'%'(Q) %13s'%'*')
    print('* %64s'%'*')
    print('* %53s'%'Current PDB:', filename, "*")
    print('*'*66)
    return None
