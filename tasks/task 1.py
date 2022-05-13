#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""

if __name__ == '__main__':
    while True:
        a = input("Первое значение: ")
        b = input("Второе значение: ")
        try:
            print(f"Результат: {int(a) + int(b)}")
        except ValueError:
            print("Результат: " + (a + b))
