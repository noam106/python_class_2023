import string
import re

class NotAStringError(Exception):

    def __init__(self):
        super().__init__(f'you entered, it is not a single letter. Please try again.')


class InvalidInputCharError(Exception):
    def __init__(self, *args: str):
        super().__init__(f'You can only pass one letter: ')



class AlphabetIterator:
    def __init__(self, letter: str):
        self._letter = letter
        self._lower_list = list(string.ascii_lowercase)
        self._upper_list = list(string.ascii_uppercase)
        self._end = 25

        if len(self._letter) > 1:
            raise InvalidInputCharError

        if self._letter not in self._lower_list and self._letter not in self._upper_list:
            raise NotAStringError


    def get_letter(self):
        return self._letter

    def get_lower_list(self):
        return self._lower_list

    def get_upper_list(self):
        return self._upper_list

    def __iter__(self):
        if self._letter in self._lower_list:
            self._counter = self._lower_list.index(self._letter)
        else:
            self._counter = self._upper_list.index(self._letter)
        return self

    def __next__(self):
        if self._counter > self._end:
            raise StopIteration()
        if self._letter in self._lower_list:
            letter_list = self._lower_list
        elif self._letter in self._upper_list:
            letter_list = self._upper_list
        letter_to_return = letter_list[self._counter]
        self._counter += 1
        return letter_to_return

if __name__ == '__main__':
    n = AlphabetIterator('h')

    for i in n:
        print(i)



