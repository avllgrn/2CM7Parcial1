from random import randrange
from os import system
from ClaseLSE import LSE

def sumaNodosEn(L):
    suma = 0
    aux = L.primero
    while aux!=None:
        suma += aux.dato
        aux=aux.siguiente
    return suma

if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(10)

    for i in range(n):
        L.insertaAlUltimo(randrange(10))

    print(f'L {L}')

    print(f'Suman {sumaNodosEn(L)}.')
