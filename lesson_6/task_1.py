#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
#  первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import sys
# os linux ubuntu 20.04 LTS 64 bit
# Первый вариант кода


def count_odd_even_1(str_num='1234567890'):
    counter_odd = 0
    counter_even = 0

    for num in str_num:

        if int(num) % 2 == 0:
            counter_odd += 1
        else:
            counter_even += 1

    # Замер памяти
    perem = (counter_even, counter_odd, num, str_num)
    memory = 0
    for var in perem:
        memory += sys.getsizeof(var)
    print(memory)

    return f"Четных {counter_odd}, Нечетных {counter_even}"

# 165 Мбайт

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

    # Замер памяти
    perem = (counter_even, counter_odd, num, digit)
    memory = 0
    for var in perem:
        memory += sys.getsizeof(var)
    print(memory)

    return f"Четных {counter_odd}, Нечетных {counter_even}"

# 108 Мбайт
# Третий способ


def count_odd_even_3(num=1234567890):
    # Замер памяти
    perem = (num,)
    memory = 0
    for var in perem:
        memory += sys.getsizeof(var)
    print(memory)
    return f"Четных: {len([y for y in str(num) if int(y) % 2 == 0])}," + \
           f" Нечетных: {len([y for y in str(num) if int(y) % 2 == 1])}"

# 32 Мбайт
# Вывод: Я буду пользоваться 3 способом, так как он использует меньше памяти


