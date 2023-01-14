from abc import ABC, abstractmethod


class Address:

    def __init__(self, street, city, floor, zipcode):
        self._street = street
        self._city = city
        self._floor = floor
        self._zipcode = zipcode

    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_floor(self):
        return self._floor

    def get_zipcode(self):
        return self._zipcode


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
                 has_balcony_door: bool, amount_upper_closets: float, amount_lower_closets: float,
                 material_work_surface: str):
        super().__init__(size, width, length, window_amount, has_balcony_door)
        self._material_work_surface = material_work_surface
        self._amount_lower_closets = amount_lower_closets
        self._amount_upper_closets = amount_upper_closets
        self._kitchen_island = False
        self._k_facilities = {
            'built-in oven': 0,
            'stove': 0,
            'dishwasher': 0,
            }

    def get_material_work_surface(self):
        return self._material_work_surface

    def set_material_work_surface(self, new_material: str):
        self._material_work_surface = new_material

    def get_amount_lower_closets(self):
        return self._amount_lower_closets

    def set_amount_lower_closets(self, new_size: float):
        self._amount_lower_closets = new_size

    def get_amount_upper_closets(self):
        return self._amount_upper_closets

    def set_amount_upper_closets(self, new_size: float):
        self._amount_upper_closets = new_size

    def get_k_facilities(self):
        return self._k_facilities

    def set_k_facilities(self, facil, num_of_facil):
        if facil in self._k_facilities:
            self._k_facilities[facil] = num_of_facil

    def get_kitchen_island(self):
        return self._kitchen_island

    def set_kitchen_island(self, is_kitchen_island: bool):
        self._kitchen_island = is_kitchen_island


class Balcony(Space):

    def __init__(self, size: float, width: float, length: float, has_gas: bool, has_water: bool):
        super().__init__(size, width, length)
        self._has_gas = has_gas
        self._has_water = has_water

    def get_has_gas(self):
        return self._has_gas

    def set_has_gas(self, is_gas: bool):
        self._has_gas = is_gas

    def get_has_water(self):
        return self._has_water

    def set_has_water(self, is_water: bool):
        self._has_water = is_water


class Flat:

    def __init__(self, address: Address, num_of_floor: int):
        self._address = address
        self._num_of_floor = num_of_floor
        self._dict_of_room: dict[str, Room] = {}
        self._dict_of_balcony: dict[str, Balcony] = {}

    def get_address(self):
        return self._address

    def get_num_of_floors(self):
        return self._num_of_floor

    def get_dict_of_room(self):
        return self._dict_of_room

    def get_floor_num(self):
        return self._address.get_floor()

    def add_room(self, size: float, width: float, length: float, windows_amount: int,
                 has_balcony_door: bool):
        num_room_place = len(self._dict_of_room) + 1
        room = Room(size, width, length, windows_amount, has_balcony_door)
        self._dict_of_room[f'room num {num_room_place}'] = room

    def add_balcony(self, size: float, width: float, length: float, has_gas: bool, has_water: bool, room_num: int):
        if room_num in self._dict_of_room:
            if self._dict_of_room[f'room num {room_num}'].get_has_balcony_door():
                self._dict_of_balcony[f'balcony for room{room_num}'] = Balcony(size, width, length, has_gas, has_water)
                return True
        else:
            return False

    def add_bathroom(self, size: float, width: float, length: float, window_amount: int,
                     has_balcony_door: bool, num_of_room_bath: str):
        if num_of_room_bath not in self._dict_of_room:
            self._dict_of_room[num_of_room_bath] = Bath(size, width, length, window_amount, has_balcony_door)
            return True
        else:
            return False

    def add_kitchen(self, size: float, width: float, length: float, window_amount: int,
                    has_balcony_door: bool, amount_upper_closets: float, amount_lower_closets: float,
                    material_work_surface: str, num_of_room_kitchen: str):
        if num_of_room_kitchen not in self._dict_of_room:
            self._dict_of_room[num_of_room_kitchen] = Kitchen(size, width, length, window_amount,
                                                              has_balcony_door, amount_upper_closets,
                                                              amount_lower_closets, material_work_surface)
            return True
        else:
            return False

    def get_flat_size(self):
        flat_size = 0
        for size in self._dict_of_room.values():
            flat_size += size.get_size()
        return flat_size

    def get_rooms_number(self):
        return len(self._dict_of_room)

    def get_balconies_number(self):
        return len(self._dict_of_balcony)

    def


