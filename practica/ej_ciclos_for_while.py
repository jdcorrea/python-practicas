# -*- coding: utf-8 -*-
# range es un ciclo for con la cantidad descrita entre parentesis


def ciclofor():
    for i in range(5):
        if i % 2 == 0:
            print("Hola, mundo Soy par: " + str(i))
        elif i == 1:
            print("Hola, mundo soy UNO")
        else:
            print("Hola, mundo NO soy par: " + str(i))


def cichowhile():
    j = 1
    while j < 10:
        print("iteración: " + str(j))
        j += 1


if __name__ == '__main__':
    ciclofor()
    cichowhile()
