# Сложность  O(n^2)
# Устойчивость - Устойчивая/Неустойчивая
# Тип - выбором
# Не требует доп. памяти

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def selection_sort(array):

    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]


selection_sort(array)
print(array)
