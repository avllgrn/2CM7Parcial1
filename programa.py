from random import randrange
from os import system
from ClaseLSE import LSE

def uneOrdenadamente(L1, L2):
    O = LSE()
    aux1=L1.primero
    aux2=L2.primero

    while aux1!=None and aux2!=None:
        if aux1.dato<=aux2.dato:
            O.insertaAlUltimo(aux1.dato)
            aux1=aux1.siguiente
        else:
            O.insertaAlUltimo(aux2.dato)
            aux2=aux2.siguiente

    while aux1!=None:
        O.insertaAlUltimo(aux1.dato)
        aux1=aux1.siguiente
    
    while aux2!=None:
        O.insertaAlUltimo(aux2.dato)
        aux2=aux2.siguiente
    

    return O

if __name__ == '__main__':
    system('cls')

    L1 = LSE()
    L2 = LSE()

    n = randrange(5,10)
    s = randrange(1, 5)
    for i in range(0,n,s):
        L1.insertaAlUltimo( i )

    n = randrange(5,10)
    s = randrange(1, 5)
    for i in range(0,n,s):
        L2.insertaAlUltimo( i )

    L3 = uneOrdenadamente(L1,L2)

    print(f'L1 {L1}')
    print('\n\n\n')
    print(f'L2 {L2}')
    print('\n\n\n')
    print(f'L3 {L3}')
    print('\n\n\n')
