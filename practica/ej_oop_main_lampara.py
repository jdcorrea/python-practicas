# -*. coding: utf-8 -*-

from ej_oop_lampara import Lamp


def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
            ¿Que deseas hacer?

            [P] Prender
            [A] Apagar
            [S] Salir ''')).upper()

        if command == 'P':
            lamp.turn_on()
        elif command == 'A':
            lamp.turn_off()
        elif command == 'S':
            break
        else:
            print('Comando no listado.')


if __name__ == '__main__':
    run()
