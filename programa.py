from random import randrange
from os import system
from ClaseLSE import LSE

def decimalAbinairo(decimal):
    L = LSE()
    while decimal!=0:
        L.insertaAlPrimero(decimal%2)
        decimal //= 2

    binario = ''
    while not L.estaVacia():
        binario += str(L.eliminaAlPrimero())

    return binario

if __name__ == '__main__':
    system('cls')

    numero = int(input('Ingresa tu número '))
    binario = decimalAbinairo(numero)

    print(f'( {numero} )10 = ( {binario} )2')

    print('\n\n\n')
