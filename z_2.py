#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Account:
    """
    Класс, представляющий банковский счет.
    """
    def __init__(self, surname="", account_number="", interest_rate=0.0, balance=0.0):
        """
        Инициализация банковского счета.
        :param surname: Фамилия владельца.
        :param account_number: Номер счета.
        :param interest_rate: Процент начисления (например, 5.5).
        :param balance: Сумма в рублях.
        """
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Сумма на счете не может быть отрицательной.")
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Процент начисления не может быть отрицательным.")

        self.surname = surname
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = float(balance)

    def read(self, prompt=None):
        """
        Ввод данных с клавиатуры.
        """
        print(prompt if prompt else "Введите данные счета:")
        self.surname = input("Фамилия владельца: ")
        self.account_number = input("Номер счета: ")
        try:
            self.interest_rate = float(input("Процент начисления: "))
            self.balance = float(input("Сумма в рублях: "))
            if self.balance < 0 or self.interest_rate < 0:
                raise ValueError
        except ValueError:
            print("Ошибка: введены некорректные числовые данные.")
            exit(1)

    def display(self):
        """
        Вывод данных на экран.
        """
        print(f"Владелец: {self.surname}")
        print(f"Номер счета: {self.account_number}")
        print(f"Процент начисления: {self.interest_rate}%")
        print(f"Баланс: {self.balance:.2f} руб.")

    def change_owner(self, new_surname):

        if not new_surname:
            raise ValueError("Фамилия не может быть пустой.")
        self.surname = new_surname
        print(f"Владелец счета изменен на: {self.surname}")

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            print("Недостаточно средств на счете.")
            return False
        self.balance -= amount
        print(f"Снято {amount:.2f} руб. Остаток: {self.balance:.2f} руб.")
        return True

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        print(f"Внесено {amount:.2f} руб. Новый баланс: {self.balance:.2f} руб.")

    def accrue_interest(self):

        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Начислено процентов: {interest:.2f} руб. Новый баланс: {self.balance:.2f} руб.")

    def to_dollars(self, rate=90.0):

        return self.balance / rate

    def to_euros(self, rate=100.0):

        return self.balance / rate

    def amount_in_words(self):
        units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
        teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
                 "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
                "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
        hundreds = ["", "сто", "двести", "триста", "четыреста",
                    "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

        rubles = int(self.balance)
        kopecks = int(round((self.balance - rubles) * 100))

        def num_to_words(n):
            if n == 0:
                return "ноль"
            result = []
            if n >= 100:
                result.append(hundreds[n // 100])
                n %= 100
            if 10 <= n < 20:
                result.append(teens[n - 10])
            else:
                if n >= 20:
                    result.append(tens[n // 10])
                    n %= 10
                if n > 0:
                    result.append(units[n])
            return " ".join(result)

        rub_text = num_to_words(rubles)
        kop_text = num_to_words(kopecks)

        # Склонение рублей
        if 11 <= rubles % 100 <= 19:
            rub_end = "рублей"
        elif rubles % 10 == 1:
            rub_end = "рубль"
        elif 2 <= rubles % 10 <= 4:
            rub_end = "рубля"
        else:
            rub_end = "рублей"

        # Склонение копеек
        if 11 <= kopecks % 100 <= 19:
            kop_end = "копеек"
        elif kopecks % 10 == 1:
            kop_end = "копейка"
        elif 2 <= kopecks % 10 <= 4:
            kop_end = "копейки"
        else:
            kop_end = "копеек"

        return f"{rub_text} {rub_end} {kop_text:02d} {kop_end}"


if __name__ == '__main__':
    print("--- Демонстрация работы класса Account ---")

    print("\n1. Создание счета:")
    acc = Account("Иванов И.И.", "40817810099910004312", 5.0, 15000.50)
    acc.display()

    print("\n2. Смена владельца:")
    acc.change_owner("Петров П.П.")
    acc.display()

    print("\n3. Пополнение счета:")
    acc.deposit(5000)
    acc.display()

    # 4. Снятие средств
    print("\n4. Снятие средств:")
    acc.withdraw(2000)
    acc.display()

    print("\n5. Начисление процентов:")
    acc.accrue_interest()
    acc.display()

    print("\n6. Перевод в валюту:")
    print(f"Сумма в долларах: {acc.to_dollars():.2f} USD")
    print(f"Сумма в евро: {acc.to_euros():.2f} EUR")

    print("\n7. Сумма прописью:")
    print(acc.amount_in_words())

    print("\n8. Ввод нового счета с клавиатуры:")
    new_acc = Account()
    new_acc.read()
    new_acc.display()
    print(f"Сумма прописью: {new_acc.amount_in_words()}")