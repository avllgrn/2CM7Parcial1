from random import randrange
from os import system
from ClaseLSE import LSE

def esPalindromo(cadena):
    L = LSE()
    cadenaAux = ''
    for caracter in cadena:
        if caracter.isalpha():
            cadenaAux+=caracter.upper()
            L.insertaAlPrimero(caracter.upper())

    for caracter in cadenaAux:
        if caracter!=L.eliminaAlPrimero():
            return False
    return True

if __name__ == '__main__':
    system('cls')

    cadena = input('Ingresa tu cadena ')
    if esPalindromo(cadena):
        print(f'{cadena} ES palíndromo')
    else:
        print(f'{cadena} NO es palíndromo')

    print('\n\n\n')
