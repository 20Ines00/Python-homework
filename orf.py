# this is our (Filips, Max's and mine) draft for the code, we thought hard and long about this, but at some point, we got stuck

from util import read_input
line_list = read_input("./orf.txt")
DNA = line_list[0]
code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G", 
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}
# here we just take the DNA string and "change" it into the RNA string
RNA = ''
for letter in DNA:
    if letter == 'T':
        RNA += 'U'
    elif letter != 'T':
        RNA += letter
print(RNA)
#this whole section is for the complementary and reversed string of DNA
def complement(x):
    if x == 'A':
        return 'T'
    elif x == 'T':
        return 'A'
    elif x == 'C':
        return 'G'
    elif x == 'G':
        return 'C'
    
reversed = DNA[::-1]
revDNA = ''
for base in reversed:
        revDNA += complement(base)
#print(revDNA)

com_rev_RNA = ''
for letter in revDNA:
        if letter == 'T':
            com_rev_RNA += 'U'
        elif letter != 'T':
            com_rev_RNA += letter
print(com_rev_RNA)

#at this point, we started to have some trouble
# the commented out stuff, which seems to repeat itself is just so I have the two codes of interest at my immediate disposal without switching between files

#def find_orfs(RNA, start):
#    locations = []
#    for i in range(len(RNA)-len(start)+1):
#        if RNA[i:i+len(start)] == start:
#            locations.append(i+1)
#    return locations
#result = find_orfs(RNA, "AUG")
#print(result)

start_codon = "AUG"
#stop_codon = ("UAA", "UAG", "UGA")
#with this we have the positions, where the "AUGs" are, but no idea how we can transform this information into the next step, which would be not taking the position but rather the "AUG" itself and build a string or list with that
def find_orfs(RNA, start_codon):
    ORF_list = []
    for i in range(len(RNA)):
        if RNA[i:i+len(start_codon)] == start_codon:
            ORF_list.append(i+1)
    return ORF_list
result = find_orfs(RNA, start_codon)
print(result)

        #codon = RNA[start:start+3]
        #aminoacid = code[codon]
        #if aminoacid == "M":
         #   print(aminoacid)
        #if aminoacid == "Stop":
        #   print(aminoacid)
    #peptide += aminoacid

#result = find_orfs(RNA, "AUG")
#print(result)

#for start in range(0, len(rna), 3):
#    codon = rna[start:start+3]
#    aminoacid = code[codon]
#    if aminoacid == "Stop":
#        break
#    peptide += aminoacid
