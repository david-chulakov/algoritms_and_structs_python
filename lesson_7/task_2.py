#  Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
#  промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:len(array)])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


array = [random.uniform(0, 50) for i in range(10)]
print(array)

print(merge_sort(array))