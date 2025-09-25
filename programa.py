from random import randrange
from os import system
from ClaseLSE import LSE

def muestraInvertida(L):
    aux1=L.primero
    aux2=L.ultimo
    
    while aux1!=aux2:
        print(f'| {aux2.dato} |', end='')
        if(aux2!=L.primero):
            print(' <- ', end='')

        while aux1.siguiente!=aux2:
            aux1=aux1.siguiente

        aux2=aux1
        aux1=L.primero

    if not L.estaVacia() and aux1==aux2:
        print(f'| {aux2.dato} |', end='')


if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(10)

    for i in range(n):
        L.insertaAlUltimo(randrange(100))

    print(f'L {L}')
    print('\n\n\n')
    muestraInvertida(L)
    print('\n\n\n')
