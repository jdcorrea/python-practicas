# -*- coding: utf-8 -*-


def average_temps(temp):
    sum_of_temps = 0

    for tmp in temp:
        print(str(tmp))
        sum_of_temps += tmp

    return sum_of_temps  # / len(temp)


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 25]
    # agregar valor a la lista
    temps.append(26)
    # quitar el último valor de la lista
    temps.pop()
    # eliminar elemento en el índice indicado
    del temps[2]
    # construir un string con una lista
    str1 = ''.join(temps)
    print('String: {}'.format(str1))

    average = average_temps(temps)
    print('La temperatura promedio es: {}'.format(average))
