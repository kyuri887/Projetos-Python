from time import sleep as sp
from random import randint as rd

def sorteia(lista):
    print('Sorteando os valores da lista: ', end='')
    for c in range(0, 5):
        cont = rd(1, 10)
        lista.append(cont)
        print(cont, end=' ', flush=True)
        sp(1)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando todos valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somapar(num)
