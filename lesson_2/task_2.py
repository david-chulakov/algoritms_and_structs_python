#  Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
#  в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

str_num = input("Введите число: ")

counter_odd = 0
counter_even = 0

for num in str_num:

    if int(num) % 2 == 0:
        counter_odd += 1
    else:
        counter_even += 1

print(f"Четных {counter_odd}")
print(f"Нечетных {counter_even}")