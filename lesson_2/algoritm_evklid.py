def nod_while(num1, num2):  # работает долго
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def nod_recursion(num1 , num2):  # рекурсия может заполнить стек
    if num2 == 0:
        return num1
    return nod_recursion(num2, num1 % num2)


def nod_while_2(num1, num2):  # нормас
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1





print(nod_while(10, 280))
print(nod_recursion(10, 280))
print(nod_while_2(10, 280))