from random import randrange
from os import system
from ClaseLSE import LSE

def cuentaNodosEn(L):
    nodos = 0
    aux = L.primero
    while aux!=None:
        nodos += 1
        aux=aux.siguiente
    return nodos

if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(10)

    for i in range(n):
        L.insertaAlUltimo(randrange(100))

    print(f'L {L}')

    print(f'Hay {cuentaNodosEn(L)} nodos.')
