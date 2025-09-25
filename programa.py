from random import randrange
from os import system
from ClaseLSE import LSE

def concatena(L1, L2):
    L3 = LSE()

    aux=L1.primero
    while aux!=None:
        L3.insertaAlUltimo(aux.dato)
        aux=aux.siguiente
    
    aux=L2.primero
    while aux!=None:
        L3.insertaAlUltimo(aux.dato)
        aux=aux.siguiente
    
    return L3

if __name__ == '__main__':
    system('cls')

    L1 = LSE()
    L2 = LSE()

    n1 = randrange(5)
    for i in range(n1):
        L1.insertaAlUltimo(randrange(100))

    n2 = randrange(5)
    for i in range(n2):
        L2.insertaAlUltimo(randrange(100))

    L3 = concatena(L1, L2)
    print(f'L1 {L1}')
    print(f'L2 {L2}')
    print(f'L3 {L3}')
    print('\n\n\n')
