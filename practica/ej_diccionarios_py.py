
def calificar():
    suma_calificaciones = 0.0
    promedio = 0.0
    calificaciones = {}
    calificaciones['algoritmos'] = 9
    calificaciones['matemáticas'] = 10
    calificaciones['web'] = 8
    calificaciones['bases_de_datos'] = 10

    for key in calificaciones.values():
        suma_calificaciones += float(key)
        print(key)

    promedio = suma_calificaciones / len(calificaciones)
    print('El promedio de calificaciones es: {}'.format(promedio))

    # for key, value in calificaciones.iteritems(): -- Python 2.x
    for key, value in calificaciones.items():
        print('llave: {}, valor: {}'.format(key, value))


if __name__ == '__main__':
    mi_diccionario = {}
    mi_diccionario['primer_elemento'] = 'Hola'
    mi_diccionario['segundo_elemento'] = 'Adios'
    print(mi_diccionario['primer_elemento'])

    calificar()
