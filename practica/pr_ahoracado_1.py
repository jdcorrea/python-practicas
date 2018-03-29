# -*- coding: utf-8 -*-
# getpass para cubrir la palabra seleccionada por el retador
import getpass


# función con lógica principal de recursividad
def ahorcado(imagen, letrasU, TurnosF, listPal, opcOk):
    # mostrar ahorcado en pantalla
    for casilla in imagen:
        ahorcadoImg = ''.join(casilla)
        print(ahorcadoImg)

    # mostrar cantidad de letras pendientes o completadas de la palabra oculta
    print(listPal)

    # Si se debe ejecutar lógica del juego
    if opcOk is True:
        print('Para finalizar el programa seleccione escriba: {}'.format('FIN'))
        ingreso = ''
        while ingreso == '':
            ingreso = input('Escoje una letra: ').lower()
        print('-' * 50)

        # en caso de que el usuario haya seleccionado la salida del juego
        if ingreso == 'fin':
            imagen = imageAhorcado(imagen)
            listPal = finFalso()
            ahorcado(imagen, letrasU, TurnosF, listPal, False)
        else:
            letra = ingreso[0]

            # Si la letra ya ha sido usada anteriormente
            if letrasU.find(letra) >= 0:
                opcOk = True
                print('La letra {} ya fue seleccionada anteriormente'.format(letra))
            # Si la letra no ha sido usada anteriormente
            else:
                listEncontrados = palabra.find(letra)
                # Si la letra no hace parte de la palabra oculta
                if listEncontrados < 0:
                    letrasU += letra
                    TurnosF += 1
                    imagen = addCuerpo(imagen, TurnosF)
                    # Si finalizó la cantidad de oportunidades
                    if TurnosF == 6:
                        print('¡¡¡Te has ahorcado, intentalo la próxima vez!!!')
                        opcOk = False
                        listPal = finFalso()
                    else:
                        opcOk = True
                # Si la letra hace parte de la palabra oculta
                else:
                    letrasU += letra

                    for indice in range(len(palabra)):
                        if palabra[indice] == letra:
                            listPal[indice] = letra

                    # Si finalizó de adivinar todas las letras de la palabra oculta
                    if finTrue(listPal) is True:
                        print('¡¡¡Felicitaciones, has adivinado la palabra!!!')
                        opcOk = False
                    else:
                        opcOk = True

            # Llamado recursivo para continuar el juego hasta fin del mismo
            ahorcado(imagen, letrasU, TurnosF, listPal, opcOk)
    # fin del juego
    else:
        print('Fin del juego')


# agregar una parte del cuerpo del ahoracado
def addCuerpo(imagen, Turnos):
    imagen = imagenRes[Turnos](imagen)
    return imagen


# agregar la cabeza del ahorcado
def cabeza(imagen):
    imagen[2][1] = '0'
    return imagen


# agregar brazo izquiero del ahorcado
def brazoIzq(imagen):
    imagen[3][0] = '/'
    return imagen


# agregar tronco del ahorcado
def tronco(imagen):
    imagen[3][1] = '|'
    return imagen


# agregar brazo derecho del ahorcado
def brazoDer(imagen):
    imagen[3][2] = '\\'
    return imagen


# agregar pie izquierdo del ahorcado
def pieIzq(imagen):
    imagen[4][0] = '/'
    return imagen


# agregar pie derecho del ahorcado
def pieDer(imagen):
    imagen[4][2] = '\\'
    return imagen


# imagen final, al salir con la palabra "fin"
def imageAhorcado(imagen):
    for i in range(6):
        imagen = addCuerpo(imagen, i + 1)
    return imagen


# palabra final, terminación no exitosa
def finFalso():
    resultado = [''] * len(palabra)
    for i in range(len(palabra)):
        resultado[i] = palabra[i]
    return resultado


# finalización exitosa?, chequeo de lista de letras adivinadas
def finTrue(listPal):
    res = True
    for i in range(len(listPal)):
        if listPal[i] == '_':
            res = False

    return res


# Diccionario de partes del cuerpo del ahorcado
imagenRes = {
    1: cabeza,
    2: tronco,
    3: brazoIzq,
    4: brazoDer,
    5: pieIzq,
    6: pieDer
}


# main del programa
if __name__ == '__main__':
    letrasUsadas = ''
    TurnosFallidos = 0
    palabra = ''
    ahorcadoini = [[' ', '+', '-', '-', '+', ' ', ' ', ' ', ' '],
                   [' ', '|', ' ', ' ', '|', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' '],
                   ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-', '-', '-']]

    while palabra == '':
        palabra = getpass.getpass("Ingrese la palabra a ser adivinida: ")

    palabra = palabra.lower()

    listPalabra = ['_'] * len(palabra)

    ahorcado(ahorcadoini, letrasUsadas, TurnosFallidos, listPalabra, True)
