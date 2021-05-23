#  В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

some_array = [-1, 2, 68, -100, -25, 2, 124, 613, -241, -3, -53]

min = 0
min_ind = 0

for i in range(len(some_array)):
    if some_array[i] < min:
        min = some_array[i]
        min_ind = i

print(some_array)
print(f'Максимлаьное отрицательное число: {min}, Индекс: {min_ind}')