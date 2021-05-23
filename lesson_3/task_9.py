#  Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

max = 0

for line in matrix:
    for num in line:
        if num > max:
            max = num

print(matrix)
print(f'Максимальное число {max}')