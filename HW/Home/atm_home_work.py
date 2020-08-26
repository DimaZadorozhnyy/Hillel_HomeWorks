from dataclasses import dataclass


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 0
    max_limit = 100000000
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.currency = 'UAH'
        self.curr_map = {'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError
        return amount

    def add_money(self, value, currency):
        self.currency = currency
        if currency == "USD":
            self.initial_amount += (value * 27)
        elif currency == "EUR":
            self.initial_amount += (value * 32)
        elif currency == "UAN":
            self.initial_amount += value

    def withdraw(self, amount, currency):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError('Превышен лимит')
        self.currency = currency
        if currency == "USD":
            self.initial_amount -= (amount * 27)
        elif currency == "EUR":
            self.initial_amount -= (amount * 32)
        elif currency == "UAH":
            self.initial_amount -= amount


money = ATM(10000)
a = input("pull - 1, push - 0")
currency_1 = input("Выберите валюту:\nUAH\nUSD\nEUR\n")

if a == "1":
    try:
        entered_amount = input("На какую сумму пополнить")
        entered_amount = int(entered_amount)
    except ValueError:
        print("Error")
    money.add_money(entered_amount, currency_1)

elif a == "0":
    try:
        entered_amount = input("Какую сумму снять?")
        entered_amount = int(entered_amount)
    except ValueError:
        print("Error")

    money.withdraw(entered_amount, currency_1)

print(money.initial_amount)
