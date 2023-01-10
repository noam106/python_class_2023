import datetime
import time


class Table:

    def __init__(self, table_id: int, num_of_seats: int):
        self._reservation_start_time = None
        self._occupied_seats = 0
        self._is_occupied = False
        self._num_of_seats = num_of_seats
        self._table_id = table_id
        self._table_location = {
            "Bar": 0,
            "Terrace": 0,
            "Indoors": 0,
            "Floor number": 0,
            "VIP room": 0,
            "less preferred": {
                "Near toilet": 0,
                'Near exit': 0,
                'Near kitchen': 0
            }
        }

    def get_reservation_start_time(self):
        return self._reservation_start_time

    def get_table_location(self):
        return self._table_location

    def get_occupied_seats(self):
        return self._occupied_seats

    def get_is_occupied(self):
        return self._is_occupied

    def get_num_of_seats(self):
        return self._num_of_seats

    def get_table_id(self):
        return self._table_id

    def update_table_location(self,table_location):
        position_list = ["Bar","Terrace","Indoors","Floor number",'VIP room']
        less_preferred = ["Near toilet", "Near exit", "Near kitchen"]
        if table_location in less_preferred:
            self._table_location["less preferred"][table_location] += 1
            return True
        elif table_location in position_list:
            self._table_location[table_location] += 1
            return True
        else:
            return False

    def reserve_a_table(self, num_of_guests):
        if self.get_is_occupied() and self._num_of_seats > num_of_guests:
            self._is_occupied = Table
            self._occupied_seats = num_of_guests
            self._reservation_start_time = datetime.datetime.now()
            return True
        else:
            return False

    def release_a_table(self):
        self._is_occupied = False
        self._occupied_seats = 0
        self._reservation_start_time = None

    def time_left(self):
        if self._is_occupied is False:
            i = datetime.datetime.now
            time_left = i - datetime.timedelta(self._reservation_start_time)
            return time_left

    def get_available_hour(self, maximum_time_limit: datetime):
        return self._reservation_start_time + datetime.datetime(maximum_time_limit)



class TableReservationSystem:

    def __init__(self, restaurant_name: str, max_time_limit: datetime, list_of_table: list):

        self._restaurant_name = restaurant_name
        self._max_time_limit = max_time_limit
        self._table_dict: dict[int, Table] = {}
        self._list_of_table = list_of_table

    def update_table_dict(self):
        for num, seats in enumerate(self._list_of_table):
            self._table_dict[num] = seats

    def get_restaurant_name(self):
        return self._restaurant_name

    def get_max_time_limit(self):
        return self._max_time_limit

    def set_max_time_limit(self, new_max_time):
        self._max_time_limit = new_max_time

    def get_table_dict(self):
        return self._table_dict

    def add_table(self, table_id: int, num_of_seat: int, table_pos: str):
        if table_id not in self._table_dict:
            self._table_dict[table_id] = Table(table_id,num_of_seat)
            self._table_dict[table_id].update_table_location(table_pos)
            return True
        else:
            return False

    def get_available_tables(self, num_of_guests):
        available_table_list = []
        for table in self._table_dict.values():
            if table.get_is_occupied() and table.get_num_of_seats() > num_of_guests:
                return available_table_list.append(table.get_table_id())

    def reserve_a_table(self, table_id: int, num_of_guest: int):
        return self._table_dict[table_id].reserve_a_table(num_of_guest)

    def release_table(self, table_id: int):
        return self._table_dict[table_id].release_a_table()

    def get_soonest_available_tables(self, num_guests: int):
        soonest_available_list = []
        for table in self._table_dict.values():
            temp_dict = {}
            if table.get_num_of_seats() >= num_guests:
                soonest_available_list.append({})
                soonest_available_list[-1][table.time_left()] = f'The table num is {table.get_table_id()},' \
                                                                f' and the num of seats are {table.get_num_of_seats()}'
        return sorted(soonest_available_list, reverse=True)




















