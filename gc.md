Given:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
= those are DNA strings in the FASTA-format, where each DNA-string has a "label" beginning with ">" and in this case Rosalind_xxxx

Result:
the DNA-string with the higest CG-content followed by the GC-content itself as a percentage

I honestly have no clue on how to solve this

BUT: maybe we could do something like linking the DNA-string to a label (because we want to have the label as result) through a dictionary, where the key is the "Rosalind_xxxx" and the value the DNA-string (maybe haha?) and then go over every key-value pair and count the bases but ignore the As and the Ts, look and/or sort for the string with the most CG-content and then somehow get this CG number into percentage (but what do I know haha).
