#  Проанализировать скорость и сложность одного любого алгоритма из разработанных
#  в рамках домашнего задания первых трех уроков.

import timeit


# Задание
# Посчитать четные и нечетные цифры введенного натурального числа.

# Первый вариант кода


def count_odd_even_1(str_num='1234567890'):
    counter_odd = 0
    counter_even = 0

    for num in str_num:

        if int(num) % 2 == 0:
            counter_odd += 1
        else:
            counter_even += 1

    return f"Четных {counter_odd}, Нечетных {counter_even}"


# Для 10 значного числа 1000 loops, best of 5: 2.04 usec per loop
# Для 30 значного числа 1000 loops, best of 5: 5.28 usec per loop
# Для 100 значного числа 1000 loops, best of 5: 17.8 usec per loop
# Для 200 значного числа 1000 loops, best of 5: 34.9 usec per loop


# Второй способ


def count_odd_even_2(num=1234567890):
    counter_odd = 0
    counter_even = 0

    while num > 0:
        digit = num % 10

        if digit % 2 == 0:
            counter_odd += 1
        else:
            counter_even += 1

        num = num // 10

    return f"Четных {counter_odd}, Нечетных {counter_even}"


# Для 10 значного числа 1000 loops, best of 5: 1.7 usec per loop
# Для 30 значного числа 1000 loops, best of 5: 4.83 usec per loop
# Для 100 значного числа 1000 loops, best of 5: 19.5 usec per loop
# Для 100 значного числа 1000 loops, best of 5: 48.2 usec per loop

# Третий способ


def count_odd_even_3(num=1234567890):
    return f"Четных: {len([y for y in str(num) if int(y) % 2 == 0])}," + \
           f" Нечетных: {len([y for y in str(num) if int(y) % 2 == 1])}"

# Для 10 значного числа 1000 loops, best of 5: 4.29 usec per loop
# Для 30 значного числа 1000 loops, best of 5: 9.97 usec per loop
# Для 100 значного числа 1000 loops, best of 5: 33.9 usec per loop


# Вывод: Я буду пользоваться 1 способом, так как он работает быстрее при больших значениях
