import sys

sys.setrecursionlimit(3000)


def akk(num1, num2):
    if num1 == 0:
        return num2 + 1
    elif num1 > 0 and num2 == 0:
        return akk(num1 - 1, 1)
    return akk(num1 - 1, akk(num1, num2 - 1))


print(akk(3, 8))