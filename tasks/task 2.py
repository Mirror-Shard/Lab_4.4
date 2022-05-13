#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Решите следующую задачу: напишите программу, которая будет генерировать матрицу из
случайных целых чисел. Пользователь может указать число строк и столбцов, а также
диапазон целых чисел. Произведите обработку ошибок ввода пользователя.
"""
from random import randint


if __name__ == '__main__':
    while True:
        try:
            cols = int(input("Введите количество столбцов: "))
            rows = int(input("Введите количество строк: "))
            min, max = map(int, input("Введите два числа - от и до: ").split())
        except ValueError:
            print(f"\033[31m !!! Вводите только числа !!!\033[38m")
            continue
        # Создаёт пустую матрицу
        A = [[0]*cols for i in range(rows)]
        # Заполняет её случайными цифрами
        for r in range(rows):
            for c in range(cols):
                A[r][c] = randint(min, max)
        # Вывод
        for r in A:
            print(r)
