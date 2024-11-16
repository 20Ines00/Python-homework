# INPUT: string s
# OUTPT: numbers A, G, C, T

# two different ways of solving the problem
def count_occurrences(word, target_letter):
    count_target_letter = 0
    for letter in word:
        if letter == target_letter:
            count_target_letter += 1
    
    return (count_target_letter)
 # this version would be faster if we had a much longer DNA-sequence         
def count_all(DNA):
    cnt_a = cnt_c = cnt_g = cnt_t = 0
    for base in DNA:
        if base == 'A':
            cnt_a += 1
        elif base == 'C':
            cnt_c += 1
        elif base == 'G':
            cnt_g += 1
        elif base == 'T':
            cnt_t += 1
    cnt_all=[cnt_a, cnt_c, cnt_g, cnt_t]
    return cnt_all


s = ''
# this print-function accords to the first version
print(count_occurrences(s,'A'), count_occurrences(s,'C'), count_occurrences(s,'G'), count_occurrences(s,'T'))
# this print-function accords to the second version
for val in count_all(s):
    print(val)