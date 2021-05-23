#   Определить, какое число в массиве встречается чаще всего.

some_array = [1, 3, 5, 5, 5, 4, 6, 7, 7, 5, 8, 1, 1, 1]

max_count = 0
max_num = 0

for num in some_array:

    if some_array.count(num) > max_count:
        max_count = some_array.count(num)
        max_num = num

print(some_array)
print(f'Чаще всех было число {num}, {max_count} раз')