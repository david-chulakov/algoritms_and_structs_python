#  Сформировать из введенного числа обратное по порядку входящих в него цифр и
#  вывести на экран. Например, если введено число 3486, надо вывести 6843.

str_num = input("Введите число: ")
some_list = []
for num in str_num:
    some_list.append(num)

print("".join(some_list[::-1]))