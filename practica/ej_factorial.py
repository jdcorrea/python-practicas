# -*- coding: utf-8 -*-


def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


if __name__ == '__main__':
    number = int(input('Escribe un número: '))

    result = fact(number)
    print(result)
