#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:

    def __init__(self, first=0, second=0):
        if first < 0 or second < 0:
            raise ValueError("Аргументы должны быть положительными числами.")
        if second >= 60:
            raise ValueError("Количество минут не может быть больше или равно 60.")
        self.first = first
        self.second = second

    def read(self):
        line = input()
        parts = list(map(int, line.split()))
        if len(parts) != 2:
            raise ValueError("Необходимо ввести два числа через пробел.")
        if parts[0] < 0 or parts[1] < 0:
            raise ValueError("Числа должны быть положительными.")
        if parts[1] >= 60:
            raise ValueError("Количество минут не может быть больше или равно 60.")
        self.first = parts[0]
        self.second = parts[1]

    def display(self):
        print(f"Часы: {self.first}, Минуты: {self.second}")

    def minutes(self):
        return self.first * 60 + self.second


def make_time(first, second):

    try:
        return Pair(first, second)
    except (ValueError, TypeError) as e:
        print(e)
        exit(1)


if __name__ == '__main__':

    print("\n make_time:")
    time1 = make_time(2, 30)
    time1.display()
    print(f"Время в минутах: {time1.minutes()}")

    print("\nконструктор Pair:")
    time2 = Pair(1, 15)
    time2.display()
    print(f"Время в минутах: {time2.minutes()}")

    print("\nввод данных с клавиатуры:")
    time3 = Pair()
    time3.read()
    time3.display()
    print(f"Время в минутах: {time3.minutes()}")
