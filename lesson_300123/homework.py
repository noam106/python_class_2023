import string
import re

class NotAStringError(Exception):

    def __init__(self, letter: str):
        super().__init__(f'you entered {letter}, it is not a single letter. Please try again.')



class AlphabetIterator:
    def __init__(self, letter: str):
        self._letter = letter
        self._lower_list = list(string.ascii_lowercase)
        self._upper_list = list(string.ascii_uppercase)
        self._end = 25

    def is_letter(self):
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
    n = AlphabetIterator('l')
    # text = AlphabetIterator('h')
    # for i in n:
    #     print(i)
    print(n.get_lower_list().index(n.get_letter()))


