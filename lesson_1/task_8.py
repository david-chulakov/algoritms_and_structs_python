# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print("Введите три разных числа")
num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num3 = int(input("Третье число: "))

if num1 > num2:
    if num2 > num3:
        print(f"Среднее число {num2}")
    else:
        if num1 > num3:
            print(f"Среднее число {num3}")
        else:
            print(f"Среднее число {num1}")
else:
    if num2 < num3:
        print(f"Среднее число {num2}")
    else:
        if num1 > num3:
            print(f"Среднее число {num1}")
        else:
            print(f"Среднее число {num3}")

