from random import randrange
from os import system
from ClaseLSE import LSE

def cadenaLSE(cadena):
    L = LSE()
    for caracter in cadena:
        L.push(caracter)
    return L

if __name__ == '__main__':
    system('cls')

    cadena = input('Ingresa tu cadena ')
    L = cadenaLSE(cadena)

    print(f'cadena: {cadena}')
    print('\n\n\n')
    print(f'L {L}')
