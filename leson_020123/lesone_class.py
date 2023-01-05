class Vehicle:
    def __init__(self, manufacturer: str, model: str, color: str, year: int, km: int = 0):
        self.__year = year
        self.__color = color
        self.__model = model
        self.__manufacturer = manufacturer
        self.__km = km

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def get_km(self):
        return self.__km


class ElectricVehicle(Vehicle):

    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 battery_capacity: int, km_per_kw: int, km: int = 0):

        super().__init__(manufacturer, model, color, year, km)

        self.__km_per_kw = km_per_kw
        self.__battery_capacity = battery_capacity
        self.__current_charge = 0

    def drive(self, km):
        available_km = self.__current_charge / self.__km_per_kw
        if available_km >= km:
            super().__km += km
            self.__current_charge -= km


class GasolineVehicle(Vehicle):

    def __init__(self, manufacturer: str, model: str, color: str, year: int,
                 tank_capacity: int, fule_consuption: int, km = 0):
        super().__init__(manufacturer, model, color, year, km)

