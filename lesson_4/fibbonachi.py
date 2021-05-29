def fib(n):
    """ рекурсивная функция нахождения числа фиббоначи
    Будет ошибка после 1000 вызовов функ
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_dict(n):
    """ рекусривная функция фиббоначи с помощью словаря(мемоизация)

    работает быстрее чем fib(n)
    Будет ошибка после 1000 вызовов функ
    """
    fib_d = {0: 0, 1: 1}

    def _fib_d(n):

        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_d(n - 1) + _fib_d(n - 2)


def fib_list(n):
    """ рекусривная функция фиббоначи с помощью списка(мемоизация)

    работает быстрее чем fib(n) и меньше памяти
    Будет ошибка после 1000 вызовов функ
    """
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_l(n):

        if fib_l[n] is None:
            fib_l[n] = fib_list(n - 1) + fib_list(n - 2)

        return fib_l[n]

    return _fib_l(n)


def fib_loop(n):
    """функция фиббоначи с помощью цикла

    работает быстрее чем fib(n) и меньше памяти
    ошибки не будет"""
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second
