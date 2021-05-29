#  Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
#  принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
#  сложность алгоритмов.


#  Поиск с помощью решето Эретосфена
def search_1(n):
    numbers = [i for i in range(2, 100)]
    for number in numbers:
        if number > 2 and number % 2 == 0:
            numbers.remove(number)
        elif number > 3 and number % 3 == 0:
            numbers.remove(number)
        elif number > 5 and number % 5 == 0:
            numbers.remove(number)
        elif number > 7 and number % 7 == 0:
            numbers.remove(number)
    return numbers[n - 1]



# Поиск 10 числа 1000 loops, best of 5: 24.5 usec per loop
# Поиск 20 числа 1000 loops, best of 5: 24.3 usec per loop
# Поиск 30 числа 1000 loops, best of 5: 27.7 usec per loop


def search_2(n):
    lst = []
    k = 0
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst[n - 1]

# Поиск 10 числа 1000 loops, best of 5: 209 usec per loop
# Поиск 20 числа 1000 loops, best of 5: 212 usec per loop
# Поиск 30 числа 1000 loops, best of 5: 220 usec per loop