import datetime
from abc import ABC, abstractmethod
from typing import List


class Transaction(ABC):

    def __init__(self, date: datetime, amount: float, currency: str, account_limit: float, exchange_rate: float,
                 usd_allowed: bool = False) -> object:
        self._date = date
        self._amount = amount
        self._currency = currency
        self._account_limit = account_limit
        self._usd_allowed = usd_allowed
        self._exchange_rate = exchange_rate
        self._nis_balance: float = 0
        self._usd_balance: float = 0

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount

    def get_currency(self):
        return self._currency

    def get_account_limit(self):
        return self._account_limit

    def set_account_limit(self, new_limit: float):
        self._account_limit = new_limit

    def get_usd_allowed(self):
        return self._usd_allowed

    def set_usd_allowed(self, permission: bool):
        self._usd_allowed = permission

    def get_nis_balance(self):
        return self._nis_balance

    def set_nis_balance(self, new_balance: float):
        self._nis_balance = new_balance

    def get_usd_balance(self):
        return self._usd_balance

    def set_usd_balance(self, new_balance: float):
        self._usd_balance = new_balance

    def get_exchange_rate(self):
        return self._exchange_rate

    def set_exchange_rate(self, new_rate: float):
        if new_rate > 0 :
            self._exchange_rate = new_rate



    def is_action_allowed(self):
        if self._currency == 'NIS' and self._amount <= self._nis_balance:
            return True
        elif self._currency == 'USD' and self._amount <= self._nis_balance:
            return True
        else:
            return False

    def deposit(self):
        if self._currency == 'NIS':
            new_balance = self._amount + self._nis_balance
            self.set_nis_balance(self, new_balance)
            return True
        elif self._currency == 'USD' and self._usd_allowed is True:
            new_balance = self._amount + self._usd_balance
            self.set_usd_balance(self, new_balance)
            return True
        else:
            return False


    def withdrawal(self):
        if self.is_action_allowed() is True:
            self._amount = self._amount * -1
            if self._currency == 'NIS':
                new_balance = self._amount + self._nis_balance
                self.set_nis_balance(self, new_balance)
                return True
            elif self._currency == 'USD' and self._usd_allowed is True:
                new_balance_1 = self._amount + self._usd_balance
                self.set_usd_balance(self, new_balance)
                return True
        else:
            return False

    def conversion(self):
        if self._usd_allowed is True:
            if self.is_action_allowed() is True:
                self._amount = self._amount * -1
                if self._currency == 'NIS':
                    usd_balance = self._amount * self._exchange_rate * -1
                    nis_balance_1 = (self._amount + self._nis_balance)
                    self.set_nis_balance(self, nis_balance_1)
                    self.set_usd_balance(self, usd_balance)
                    return True
                elif self._currency == 'USD' and self._usd_allowed is True:
                    usd_balance_1 = self._amount + self._usd_balance
                    self.set_usd_balance(self, usd_balance_1)
                    nis_balance = (1 / self._exchange_rate) * self._amount * -1
                    self.set_nis_balance(self, nis_balance)
                    return True
            else:
                return False






    @abstractmethod
    def action(self):
        pass


class Deposit(Transaction):

    def __init__(self, date: datetime, amount: float, currency: str, account_limit: float, usd_allowed: bool = False):
        super().__init__(date, amount, currency, account_limit, usd_allowed=False)

        self._deposit_log = {}

    def action(self) -> bool:
        if super().is_action_allowed() is True:
            if self._date in self._deposit_log:
                self._deposit_log[self._date].append(f'deposit amount is {self._amount}',
                                                    f"The currncy is {self.currency}")
            else:
                self._deposit_log[self._date] = []
                self._deposit_log[self._date].append(f'deposit amount is {self._amount}',
                                                    f"The currncy is {self.currency}")
            return True
        else:
            return False


class Withdrawal(Transaction):

    def __init__(self, date: datetime, amount: float, currency: str, account_limit: float, usd_allowed: bool = False):
        super().__init__(date, amount, currency, account_limit, usd_allowed=False)

        self._withdrawal_log = {}

    def action(self)-> bool:

        if super().is_action_allowed() is True:
            if self._date in self._withdrawal_log:
                self._withdrawal_log[self._date].append(f'Withdrawal amount is {self._amount}',
                                                       f"The currncy is {self.currency}")
            else:
                self._withdrawal_log[self._date] = []
                self._withdrawal_log[self._date].append(f'Withdrawal amount is {self._amount}',
                                                       f"The currncy is {self.currency}")
            return True
        else:
            return False

class Conversion(Transaction):

    def __init__(self, date: datetime, amount: float, currency: str, account_limit: float, exchange_rate: float, usd_allowed: bool = False):
        super().__init__(date, amount, currency, account_limit, exchange_rate, usd_allowed=False)

        self._conversion_log = {}

    def action(self) -> bool:
        if self.is_action_allowed() is True:
            if self._date in self._conversion_log:
                if super()._currency == "USD":
                    self._conversion_log[self._date].append(f'converted from {self._currency} to NIS the amount of {self._amount} in the exchange_rate of {self._exchange_rate}')
                elif super()._currency == "NIS":
                    self._conversion_log[self._date].append(f'converted from {self._currency} to USD the amount of {self._amount} in the exchange_rate of {1 / self._exchange_rate}')
                return True
            else:
                self._conversion_log[self._date] = []
            if super()._currency == "USD":
                self._conversion_log[self._date].append(f'converted from {self._currency} to NIS the amount of {self._amount} in the exchange_rate of {self._exchange_rate}')
            elif super()._currency == "NIS":
                self._conversion_log[self._date].append(f'converted from {self._currency} to USD the amount of {self._amount} in the exchange_rate of {1 / self._exchange_rate}')
            return True
        else:
            return False


# leetcode:
# 1
# class Solution:
#
#     def __init__(self, word: str):
#         self._word = word
#
#     def maxNumberOfBalloons(self, text: str) -> int:
#         leter_in_word = []
#         count = 0
#         for i in text:
#             if i in self._word:
#                 leter_in_word.append(i)
#         while len(leter_in_word) > 0:
#             word = ""
#             for i in self._word:
#                 if i in leter_in_word:
#                     word += i
#                     leter_in_word.remove(i)
#                     if word == self._word:
#                         count += 1
#         return count
#
#
# #2
#
# # class Solution_1:
#
# def maxProfit( prices: List[int]) -> int:
#     num_of_prices = len(prices)
#     output_1 = 0
#     for place, i in enumerate(prices):
#         if num_of_prices - 1 == place:
#             return output_1
#         else:
#             ret_val = (max(prices[place+1::])) - i
#             if ret_val > output_1:
#                 output_1 = ret_val
#     return output_1
#
#
# print(maxProfit(prices = [7,1,5,3,6,4]))


# 3
