# #d4
# # 1

import string
import datetime


def letter_to_num(letter_list: list[str]) -> list:
    lowercase_list = []
    alphabet = list(string.ascii_lowercase)
    filter_list = filter(lambda letter: letter.lower() in alphabet, letter_list)
    result = list(map(lambda letter: alphabet.index(letter.lower()) + 1, filter_list))
    return result

print(letter_to_num(['a', 'Z', 'c', '1']))

# # 2
#
# def vowels_destroyer(letter: str) -> bool:
#     vowels_tuple = ('e', 'a', 'i', 'o', 'u')
#     if letter.lower() not in vowels_tuple:
#         return True
#
# word = "hello"
# x = "".join(filter(vowels_destroyer, word))
#
#
# print(x)
import datetime


# 3

def str_to_date(word: str) -> datetime:
    new_date = datetime.datetime.strptime(word, '%d-%m-%Y')
    return new_date


def is_sat_or_fri(day: datetime) -> bool:
    if datetime.date.weekday(day) == 4 or datetime.date.weekday(day) == 5:
        return False
    else:
        return True


date_list = ['12-12-2021', '18-12-2021', '19-12-2021']


new_date_list = list(map(str_to_date, date_list))
filtered_list = list(filter(is_sat_or_fri, new_date_list))
print(filtered_list)

# 4

str_list = ['asd', 'asdf', 'kjhgf', 'sdfsdfsdf']
y = list(sorted(str_list, key=len))
print(y)


# 5

def order_grades(log_dict: list):
    grades_order_tuple = ['great', 'good', 'bad']
    x = list(sorted(log_dict, key=lambda word: [grades_order_tuple.index(word)], ))
    return x

def order_by_time(log_dict: list):
    x = list(map(datetime.datetime.strptime()))

print(order_grades(['great', 'good', 'bad','great', 'good', 'bad','great', 'good', 'bad']))

# 6


def homework_6(list_of_words: list[str]) -> list:
    result = list(filter(lambda word: word.count('a') not in (0,1), list_of_words))
    return result

print(homework_6( ["apple", "ananas", "banana", "pear"]))
