from random import randrange
from os import system
from ClaseLSE import LSE

def esPrimo(n):
    if n==0 or n==1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True

def cuentaPrimosEn(L):
    pares = 0
    aux = L.primero
    while aux!=None:
        if esPrimo(aux.dato) != 0:
            pares += 1
        aux=aux.siguiente
    return pares

if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(10)

    for i in range(n):
        L.insertaAlUltimo(randrange(10))

    print(f'L {L}')

    print(f'Hay {cuentaPrimosEn(L)} primo(s).')
