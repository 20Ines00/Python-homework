>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

given: a DNA string in the fasta-format
output: multiple reading frames

idea: reading frames start at a "start"-codon and and with "stop"-codons --> 
number 1: the DNA string should firstly be translated into an RNA string (codons have "U" instead of "T")
number 2: copy the codon dictionary
number 3: take the loop from there as well and loop over the (now) RNA string in pairs of three
number 4: inside the loop with if-statements, take the three bases, that symbolize the start, from there translate the bases after that into proteins until to one of the stop-codons and save all that in an (before made) empty string  