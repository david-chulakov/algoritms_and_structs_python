# Сложность - O(n^2) / O(n * log(n))
# Устойчивость - Неустойчивая
# Тип - Обменная
# Потребление памяти O(n) / Не требует доп.памяти

import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    l_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

new_array = quick_sort(array)
print(new_array)


def quick_sort_no_memory(array, first, last):

    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i, j = first, last

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, first, j)
    quick_sort_no_memory(array, i, last)


quick_sort_no_memory(array, 0, len(array) - 1)
print(array)
