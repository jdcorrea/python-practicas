'''def run():
    with open('numeros.txt', 'w', encoding='utf-8') as f:
        for i in range(11):
            f.write(str(i))'''


def run():
    counter = 0
    with open('aleph.txt', encoding='utf-8') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz de encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()
