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

def sumaNodosEn(L):
    suma = 0
    aux = L.primero
    while aux!=None:
        suma += aux.dato
        aux=aux.siguiente
    return suma

def cuentaMenoresAPromedioEn(L):
    promedio = sumaNodosEn(L) / cuentaNodosEn(L)
    nodos = 0
    aux = L.primero
    while aux!=None:
        if aux.dato<promedio:
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
    print('\n\n\n')

    print(f'Hay {cuentaNodosEn(L)}.')
    print(f'Suman {sumaNodosEn(L)}.')
    if n>0:
        print(f'El promedio es { sumaNodosEn(L) / cuentaNodosEn(L)}.')
        print(f'Hay {cuentaMenoresAPromedioEn(L)} menores que el promedio.')
    print('\n\n\n')
