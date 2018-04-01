# -*- coding: utf-8 -*-


def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
    numbers = [51, 3, 49, 5, 25, 9, 10, 11, 6, 27, 28, 34, 36, 4, 1]
    numbers.sort()
    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número está en la lista')
    else:
        print('El número no está en la lista')
