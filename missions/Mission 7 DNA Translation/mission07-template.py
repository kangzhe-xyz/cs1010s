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
    """Your code here"""

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
    """Your code here"""

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
    """Your code here"""

def reverse_transcribe(rna_strand):
    """Your code here"""

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
    """Your code here"""

print("## Q4 ##")
codon2amino = get_mapping("codon_mapping.csv")

# Uncomment to test your function
# print(codon2amino["ACA"]) # 'T'
# print(codon2amino["AUU"]) # 'I'
# print(codon2amino["CUC"]) # 'L'
# print(codon2amino["ACU"]) # 'T'
# print(codon2amino["UAG"]) # '_'
# print(codon2amino["UGA"]) # '_'


##########
# Task 5 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    """Your code here"""

print("## Q5 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_'
print(protein == 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_') # True
