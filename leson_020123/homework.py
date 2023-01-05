from abc import ABC
from datetime import datetime


class Transaction(ABC):
    def __init__(self, date: datetime, currency: str, account_limit: float = 0):
        self._account_limit = account_limit
        self._currency = currency
        self._date = date

    def get_currency(self):
        return self._currency

    def get_date(self):
        return self._date

    def get_account_limit(self):
        return self._account_limit

    def set_account_limit(self, new_limit: float):
        self._account_limit = new_limit


class Deposit(Transaction):
    def __init__(self, date: datetime, currency: str, deposit_amount, account_limit: float = 0):
        super().__init__(date, currency)

        self._account_limit = account_limit
        self._deposit_amount = deposit_amount

    def actaion(self):

