"""Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число"""

import sys
sys.set_int_max_str_digits(0)


def seq_fibonacci():
    prev_num = 1
    num = 0
    count = 1
    while True:
        yield num, count
        count += 1
        next_num = prev_num + num
        prev_num = num
        num = next_num

for num, count in seq_fibonacci():
    if count in (5, 200, 1000, 100000):
        print(num)
        if count == 100000:
            break
