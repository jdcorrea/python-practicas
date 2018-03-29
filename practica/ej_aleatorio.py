import random


def run(less, higher):

    number_found = False
    random_number = random.randint(less, higher)
    intentos = 0
    while not number_found:
        intentos = intentos + 1
        number = int(input('intenta un nemero: '))
        if number == random_number:
            print('Encontraste el numero')
            print('total de intentos: {}'.format(intentos))
            number_found = True
        elif number > random_number:
            print('El numero es mas pequeño')
        else:
            print('El Numero Es Mas Grande')


if __name__ == '__main__':

    less = int(input('Ingrese el numero con menor valor : '))
    print('')
    higher = int(input('ingrese el numero con mayor valor : '))
    print('')
    run(less, higher)
