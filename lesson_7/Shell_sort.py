# Сложность O(n^2) / O(n * log(n)^2 / O(n^3/2)
# Устойчивость - неустойчивая
# Тип - вставками
# Не требует доп.памятит

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def shell_sort(array):

    assert len(array) < 4000, 'Array is too big'

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment-1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                print(array)

shell_sort(array)
print(array)