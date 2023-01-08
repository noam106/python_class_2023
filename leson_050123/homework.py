from abc import ABC, abstractmethod


class Space(ABC):

    def __init__(self, size: float, width: float, length: float):
        self._size = size
        self._width = width
        self._length = length

    def get_size(self):
        return self._size

    def set_size(self):
        self._size = self._length * self._width

    def get_width(self):
        return self._width

    def set_width(self, new_width):
        self._width = new_width

    def get_length(self):
        return self._length

    def set_length(self, new_length):
        self._length = new_length

class Room(Space):


    def __init__(self, ):
