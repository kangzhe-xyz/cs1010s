# CS1010S --- Programming Methodology
# Mission 7

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    res = ""
    for i in dna_strand:
        res += dna_base_pairings[i]
    return res[::-1]

print("## Q1 ##")
print(replicate("AAATGC"))     # 'GCATTT'
print(replicate("ATTGGGCCCC")) # 'GGGGCCCAAT'

with open("dna.txt") as f:
    dna = f.read()
print(replicate(dna)[:10])    #'AATAGTTTCT'


##########
# Task 2 #
##########

def find_transcription_region(dna_strand):
    """
    returns the region to transcribe. detects "TATA" (excl) and "CGCG" (incl) sequence, returns things between.
    """
    for i in range(len(dna_strand)):
        if len(dna_strand) - i < 4: # if less than 4 chars left in the string, not possible for TATA
            return None
        elif dna_strand[i:i+4:1] == "TATA": # check i to i+3
            result = dna_strand[i+4::] # return the remaining
            break
    
    if not "CGCG" in result:
        return result

    else: 
        result2 = ""
        for i in range(len(result)):
            if not result[i:i+4:1] == "CGCG":
                result2 += result[i]
            else:
                return result2 + "CGCG"
        return result2

print("## Q2 ##")
print(find_transcription_region("AGCTTAGCTATATCGTTAATTGCAGAGACGCGA"))
# 'TCGTTAATTGCAGAGACGCG'
print(find_transcription_region("TATAAGCTTAGCTATATAGCGTACAGTCCGCGACGCG"))
# 'AGCTTAGCTATATAGCGTACAGTCCGCG'
print(find_transcription_region("AGCGAGCGTAGC"))
# None


##########
# Task 3 #
##########

def transcribe(dna_strand):
    dna_strand = find_transcription_region(dna_strand)
    rna_base_pairings = {
        "A": "U",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    result = ""
    for i in dna_strand:
        result += rna_base_pairings[i]
    return result[::-1]

def reverse_transcribe(rna_strand):
    reverse_rna_base_pairings = {
        "A": "T",
        "U": "A",
        "C": "G",
        "G": "C"
    }
    result = ""
    for i in rna_strand:
        result += reverse_rna_base_pairings[i]
    return result[::-1]

print("## Q3 ##")
print(transcribe("AGCTTAGCTATATCGTTAATTGCAGAGACGCGA"))
 # 'CGCGUCUCUGCAAUUAACGA'
print(transcribe("TATAATTGGGCCCCCGCG"))
 # 'CGCGGGGGCCCAAU'

print(reverse_transcribe("CGCGUCUCUGCAAUUAACGA")) 
# 'TCGTTAATTGCAGAGACGCG'
print(reverse_transcribe("CGCGGGGGCCCAAU")) 
# 'ATTGGGCCCCCGCG'

rna = transcribe(dna)
print(rna[:10])
# 'CGCGGCAUAG'
print(reverse_transcribe('CGCGGCAUAG'))
# 'CTATGCCGCG'


##########
# Task 4 #
##########

def get_mapping(csvfilename):
    tpls = read_csv(csvfilename)
    aa_mappings = {}
    for i in tpls:
        aa_mappings[i[0]] = i[-1]
    return aa_mappings


print("## Q4 ##")
codon2amino = get_mapping("codon_mapping.csv")

# Uncomment to test your function
print(codon2amino["ACA"]) # 'T'
print(codon2amino["AUU"]) # 'I'
print(codon2amino["CUC"]) # 'L'
print(codon2amino["ACU"]) # 'T'
print(codon2amino["UAG"]) # '_'
print(codon2amino["UGA"]) # '_'


##########
# Task 5 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    if "AUG" not in rna_strand: # no start codon, skip the check altogether
        return None
    else:
        while rna_strand[0:3] != "AUG": # keep deleting the first char until "AUG" is the first 3
            if rna_strand == "":
                return None
            rna_strand = rna_strand[1:]
        
        protein = "" # init empty string
        for i in range(0, len(rna_strand), 3): # sliding window every 3 chars
            if "_" not in protein:
                protein += codon2amino[rna_strand[i:i+3:1]] # add the lookup result
            else: # hits "_", return
                return protein
        return protein if protein[-1] == "_" else None # no stop codon, invalid protein

print("## Q5 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_'
print(protein == 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_') # True
