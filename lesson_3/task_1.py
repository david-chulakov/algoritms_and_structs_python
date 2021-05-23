#  В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
#  Примечание: 8 разных ответов.

multiple_2 = []
multiple_3 = []
multiple_4 = []
multiple_5 = []
multiple_6 = []
multiple_7 = []
multiple_8 = []
multiple_9 = []


for i in range(2, 100):
    if i % 2 == 0:
        multiple_2.append(i)
        if i % 4 == 0:
            multiple_4.append(i)
        if i % 6 == 0:
            multiple_6.append(i)
        if i % 8 == 0:
            multiple_8.append(i)
        if i % 5 == 0:
            multiple_5.append(i)
        if i % 7 == 0:
            multiple_7.append(i)
        if i % 3 == 0:
            multiple_3.append(i)
        if i % 9 == 0:
            multiple_9.append(i)
    elif i % 3 == 0:
        multiple_3.append(i)
        if i % 9 == 0:
            multiple_9.append((i))
    elif i % 5 == 0:
        multiple_5.append(i)
    elif i % 7 == 0:
        multiple_7.append(i)

print(f'Кратны 2: {multiple_2}')
print(f'Кратны 3: {multiple_3}')
print(f'Кратны 4: {multiple_4}')
print(f'Кратны 5: {multiple_5}')
print(f'Кратны 6: {multiple_6}')
print(f'Кратны 7: {multiple_7}')
print(f'Кратны 8: {multiple_8}')
print(f'Кратны 9: {multiple_9}')
