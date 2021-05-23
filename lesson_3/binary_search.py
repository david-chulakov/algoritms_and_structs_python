#  бинарный поиск используется для упорядоченных массивов

def bin_search(sorted_array, value):
    """ Функция бинарного поиска

    :param sorted_array: остортированный массив
    :param value: искомое значение
    :return: индекс искомого значение или None если его нет
    """

    left = 0
    right = len(sorted_array) - 1
    pos = (left + right) // 2

    while sorted_array[pos] != value and left <= right:

        if value > sorted_array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return None if left > right else pos


some_list = [i for i in range(36) if i % 2 == 0]
print(some_list)
print(bin_search(some_list, 6))
print(bin_search(some_list, 5))