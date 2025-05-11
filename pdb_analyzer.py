import os

class PDBAnalyzer:
    """Main class for PDB file analysis operations"""
    
    def __init__(self, filename=None):
        self.filename = filename
        self.title = ""
        self.chains = {}
        self.helix_counts = {}
        self.sheet_counts = {}
        self.amino_sequences = {}
        self.amino_codes = {
            "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "ASX": "B",
            "CYS": "C", "GLU": "E", "GLN": "Q", "GLX": "Z", "GLY": "G",
            "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M",
            "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
            "TYR": "Y", "VAL": "V"
        }
        if filename:
            self.load_file(filename)

    def load_file(self, filename):
        """Load and parse a PDB file"""
        self.filename = filename
        self.title = ""
        self.chains.clear()
        self.helix_counts.clear()
        self.sheet_counts.clear()
        self.amino_sequences.clear()

        with open(filename, 'r') as file:
            whole_file = file.readlines()
            self._parse_pdb_content(whole_file)

    def _parse_pdb_content(self, content):
        """Parse the content of PDB file"""
        whole_seq_string = ""
        
        for line in content:
            if line.startswith("TITLE"):
                self.title += line[10:]
            elif line.startswith("SEQRES"):
                chain_id = line[11]
                if chain_id not in self.chains:
                    self.chains[chain_id] = int(line[13:19])
                
                # Process amino acid sequence
                seq_parts = line.split()[4:]  # Skip first 4 parts to get amino acids
                for aa in seq_parts:
                    if aa in self.amino_codes:
                        whole_seq_string += self.amino_codes[aa]
                
                if chain_id not in self.amino_sequences:
                    self.amino_sequences[chain_id] = ""
                self.amino_sequences[chain_id] = whole_seq_string
                
            elif line.startswith("HELIX"):
                chain_id = line[19:20]
                self.helix_counts[chain_id] = self.helix_counts.get(chain_id, 0) + 1
                
            elif line.startswith("SHEET"):
                chain_id = line[32:33]
                self.sheet_counts[chain_id] = self.sheet_counts.get(chain_id, 0) + 1

    def get_info(self):
        """Display comprehensive information about the PDB file"""
        print(f"Title: {self.title}")
        print(f"CHAINS: {' and '.join(self.chains.keys())}")
        
        for chain_id, aa_count in self.chains.items():
            print(f"--Chain {chain_id}")
            print(f"Number of amino acids: {aa_count}")
            print(f"Number of helix: {self.helix_counts.get(chain_id, 0):>7}")
            print(f"Number of sheet: {self.sheet_counts.get(chain_id, 0):>7}")
            
            if chain_id in self.amino_sequences:
                sequence = self.amino_sequences[chain_id]
                print("Sequence:")
                for i in range(0, len(sequence), 50):
                    print(" " * 18 + sequence[i:i+50])

    def get_secondary_structure(self):
        """Analyze and display secondary structure"""
        with open(self.filename, 'r') as file:
            content = file.readlines()
            sheet_dict = {}
            helix_dict = {}
            chain_dict = {}
            representation_dict = {}
            
            # Parse file for secondary structure
            for line in content:
                if line.startswith("SHEET"):
                    sheet_tag = line[8:10] + line[12:14]
                    sheet_dict[sheet_tag] = (line[21], int(line[23:26]), int(line[34:37]))
                    
                elif line.startswith("HELIX"):
                    helix_tag = line[12:14]
                    helix_dict[helix_tag] = (line[19], int(line[21:25]), int(line[34:37]))
                    
                elif line.startswith("SEQRES"):
                    chain_id = line[11:12]
                    chain_dict.setdefault(chain_id, int(line[13:18]))
                    
            # Create initial representation
            for key, value in chain_dict.items():
                representation_dict[key] = list(value * "-")
            
            # Process sheets
            for k in sheet_dict.values():
                replist = representation_dict[k[0]]
                del replist[k[1]:k[2]+1]
                for _ in range(k[2] - k[1]+1):
                    replist.insert(k[1]-1, '|')
                    
            # Process helices
            for k in helix_dict.values():
                replist = representation_dict[k[0]]
                del replist[k[1]:k[2]+1]
                for _ in range(k[2] - k[1]+1):
                    replist.insert(k[1]-1, '/')
                    
            print(f"Secondary structure of the PDB id: {self.filename}")
            for key, value in representation_dict.items():
                print(f"Chain: {key}")
                final_representation = ''.join(value)
                for i in range(0, len(final_representation), 80):
                    print(final_representation[i:i+80])
                print(len(final_representation))

    def get_histogram(self, sort_type="aa"):
        """Generate amino acid histogram with specified sorting"""
        amino_counts = self._count_amino_acids()
        
        if sort_type == "aa":  # alphabetically ascending
            items = sorted(amino_counts.items())
        elif sort_type == "da":  # alphabetically descending
            items = sorted(amino_counts.items(), reverse=True)
        elif sort_type == "an":  # numerically ascending
            items = sorted(amino_counts.items(), key=lambda x: x[1])
        elif sort_type == "dn":  # numerically descending
            items = sorted(amino_counts.items(), key=lambda x: x[1], reverse=True)
        else:
            raise ValueError("Invalid sort type")
            
        for aa, count in items:
            if count > 0:
                print(f"{aa} : {'*' * count}")

    def _count_amino_acids(self):
        """Count occurrences of each amino acid in the PDB file"""
        amino_counts = {
            "ALA": 0, "ARG": 0, "ASN": 0, "ASP": 0, "ASX": 0, "CYS": 0,
            "GLU": 0, "GLN": 0, "GLX": 0, "GLY": 0, "HIS": 0, "ILE": 0,
            "LEU": 0, "LYS": 0, "MET": 0, "PHE": 0, "PRO": 0, "SER": 0,
            "THR": 0, "TRP": 0, "TYR": 0, "VAL": 0
        }
        
        with open(self.filename, 'r') as file:
            content = file.readlines()
            seq_string = ""
            
            for line in content:
                if line.startswith("SEQRES"):
                    seq_string += line[17:70]
                    
            amino_list = [aa for aa in seq_string.split() if aa]
            for aa in amino_list:
                if aa in amino_counts:
                    amino_counts[aa] += 1
                    
        return amino_counts

    @staticmethod
    def is_valid_pdb_file(filename):
        """
        Validate if the given file is a proper PDB file by checking for essential PDB format elements.
        
        Returns:
        - (bool, str): A tuple containing (is_valid, error_message)
        Raises:
        - FileNotFoundError: If the file doesn't exist
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
            
        required_records = {'HEADER', 'TITLE', 'COMPND'}
        found_records = set()
        
        try:
            with open(filename, 'r') as file:
                # Read first 20 lines to check for essential records
                first_lines = [file.readline() for _ in range(20)]
                
                # Check if file is empty
                if not first_lines:
                    return False, "File is empty"
                
                # Check for required record types
                for line in first_lines:
                    if not line.strip():
                        continue
                        
                    # Check if lines follow PDB format (fixed width format)
                    if len(line) < 80:  # PDB lines should be at least 80 characters when padded
                        continue
                    
                    record_type = line[0:6].strip()
                    if record_type in required_records:
                        found_records.add(record_type)
                
                # Continue reading rest of file to check for ATOM/HETATM records
                has_structure = False
                for line in file:
                    if line.startswith(('ATOM  ', 'HETATM')):
                        has_structure = True
                        break
                
                missing_records = required_records - found_records
                
                if missing_records:
                    return False, f"Missing required PDB records: {', '.join(missing_records)}"
                
                if not has_structure:
                    return False, "No structural data (ATOM/HETATM records) found"
                
                return True, "Valid PDB file"
                
        except UnicodeDecodeError:
            return False, "File contains invalid characters (not a text file)"
        except Exception as e:
            return False, f"Error reading file: {str(e)}"
