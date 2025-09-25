from random import randrange
from os import system
from ClaseLSE import LSE

def esCapicua(numero):
    L = LSE()
    for caracter in numero:
        L.insertaAlPrimero(caracter)

    for caracter in numero:
        if caracter!=L.eliminaAlPrimero():
            return False
    return True

if __name__ == '__main__':
    system('cls')

    numero = input('Ingresa tu numero ')
    if esCapicua(numero):
        print(f'{numero} ES capicúa')
    else:
        print(f'{numero} NO es capicúa')

    print('\n\n\n')
