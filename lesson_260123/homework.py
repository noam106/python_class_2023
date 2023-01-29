#
# # f1
# # 1
# def is_word_capitalized(word: str) -> bool:
#     if word[0].isupper() and word[1].islower():
#         return True
#     else:
#         return False
#
# # print(is_word_capitalized('NNam'))
#
# # 2

def tata_box_pattern(dna_string: str) -> bool:
    nucleotide_tuple = ('A', 'C', 'G', 'T')
    for nuc in dna_string:
        if nuc not in nucleotide_tuple:
            return 'not proper DNA sepuence'

    start_sequence = ('TATAA')
    end_sequence = ('TT')
    if start_sequence in dna_string and end_sequence in dna_string:
        tata_pos = (dna_string.index('TATAA'))
        if dna_string[tata_pos + 8] == 'T' and dna_string[tata_pos + 9] == 'T':
            return True
        else:
            return False

dna = "ACGACGTTTACACGGAAATAAGGGTACGCGCTGTATAATGTTTGATCAGCTGATTCGAA"
# print( 'TATAA' in dna)
# print(type(dna.index('TATAA')))

print(tata_box_pattern(dna))