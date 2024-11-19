# INPUT: DNA-string s
# OUTPUT: RNA-string 

rna = ''
for letter in s:
    if letter == 'T':
        rna += 'U'
    elif letter != 'T':
        rna += letter

print(rna)

