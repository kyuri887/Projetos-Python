from math import factorial
from time import sleep

def fatorial():
    n = int(input('Digite um número para fazer o calculo fatorial: '))
    print('Processando...')
    sleep(3)
    f = factorial(n)
    print(f'{n}! = ',end='')
    while n >= 1:
        if n > 1:
            print(f'{n}',end=' x ')
        else:
            print(f'{n}',end=f' = {f}\n')
        n-=1

while True:
    consultar = fatorial()
    consultar = str(input('Quer consultar novamente?(S/N): '))
    print('Processando...')
    sleep(2)
    while consultar not in ['s','S','n','N']:
        print('Valor não compreendido, TENTE NOVAMENTE!')
        sleep(2.5)
        consultar = str(input('Quer consultar novamente?(S/N): '))
        print('Processando...')
        sleep(2)
    if consultar in ['s', 'S']:
        pass
    elif consultar in ['n', 'N']:
        break
    else:
        break
print('Fim do programa')

        
        
