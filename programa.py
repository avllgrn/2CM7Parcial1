from random import randrange
from os import system
from ClaseLSE import LSE

def generaInvertida(L):
    I = LSE()
    aux=L.primero
    while aux!=None:
        I.insertaAlPrimero(aux.dato)
        aux=aux.siguiente

    return I

if __name__ == '__main__':
    system('cls')

    L1 = LSE()

    n = randrange(10)

    for i in range(n):
        L1.insertaAlUltimo(randrange(100))

    print(f'L1 {L1}')
    print('\n\n\n')
    L2 = generaInvertida(L1)
    print(f'L2 {L2}')
    print('\n\n\n')
