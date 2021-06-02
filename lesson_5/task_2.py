from collections import defaultdict
from collections import deque


def my_dex(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def my_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = my_dex(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = my_dex(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')