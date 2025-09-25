from random import randrange
from os import system
from ClaseLSE import LSE

def cuentaParesEn(L):
    pares = 0
    aux = L.primero
    while aux!=None:
        if aux.dato%2 == 0:
            pares += 1
        aux=aux.siguiente
    return pares

if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(10)

    for i in range(n):
        L.insertaAlUltimo(randrange(100))

    print(f'L {L}')

    print(f'Hay {cuentaParesEn(L)} par(es).')
