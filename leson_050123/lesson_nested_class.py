class Person:
    def __init__(self, id_num: int, name: str, last_name: str, middle_name: str = "",
                 adress = Adress):
        self._adress = adress
        self._middle_name = middle_name
        self._last_name = last_name
        self._name = name
        self._id_num = id_num

    def get_adress(self):
        return self._adress

    def set_adress(self, new_adress: Adress):
        self._adress = new_adress

    def get_middel_name(self):
        return self._middle_name

    def set_middle_name(self, new_name: str):
        self._middle_name = new_name

    def set_last_name(self, new_name):
        self._last_name = new_name

    def get_last_name(self):
        return self._last_name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"<{self._name},{self._last_name},{self._id_num}>"



