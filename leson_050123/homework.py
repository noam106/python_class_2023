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

    def __init__(self, size: float, width: float, length: float, windows_amount: int,
                 has_balcony_door: bool):
        super().__init__(size, width, length)
        self._window_amount = windows_amount
        self._has_balcony_door = has_balcony_door

    def get_has_balcony_door(self):
        return self._has_balcony_door

    def get_window_amount(self):
        return self._window_amount


class Bath(Room):

    def __init__(self, size: float, width: float, length: float, window_amount: int,
                 has_balcony_door: bool):
        super().__init__(size, width, length, window_amount, has_balcony_door)

        self._facilities = {
            'toilet': 0,
            'sink': 0,
            'bath': 0,
            'shower': 0
        }

    def get_facilities(self):
        return self._facilities

    def set_facilities(self, facil, num_of_facil):
        if facil in self._facilities:
            self._facilities[facil] = num_of_facil


class Kitchen(Room):

    def __init__(self, size: float, width: float, length: float, window_amount: int,
                 has_balcony_door: bool):
        super().__init__(size, width, length, window_amount, has_balcony_door)

