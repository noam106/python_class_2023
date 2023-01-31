import re


# print(re.search('((cat )*| {1}|(dog)*)', "catcat dog dog dog cat" ))

# f1

# 1
def is_capitol(name: str) -> bool:
    if re.search("[A-Z][a-z]*",name):
        return True
    return False


print(is_capitol('noam'))

#2


def is_tataa(dna: str) -> bool:
    if re.search('(TATAA)[A|C|G|T]{3}(AA)', dna):
        return True
    return False


dna = "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"
print(is_tataa(dna))


def two_dig_two_char(char: str) -> bool:
    if re.search('[0-9]{2}.[^0-9]{2}', char):
        return True
    return False


print(two_dig_two_char('98okh'))

#4

#7
def cellphone_num(israeli_cell: str) -> bool:
    if re.search('^(05)[0-9]-[0-9]{7}', israeli_cell):
        return True
    return False


print(cellphone_num('052-8419897'))


# 6
def three_digit(num_str: str) -> bool:
    if re.search('[0-9] ?[0-9] ?[0-9]', num_str):
        return True
    return False

print(three_digit('3 52fdf564'))




