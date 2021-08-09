from math import factorial
from time import sleep

def fatorial():
    n = int(input('Digite um número para calcular o seu fatorial: '))
    print('Processando...')
    sleep(3)
    f = factorial(n)
    contador = n
    print(f'{n}! = ',end='')
    while contador > 0:
        if contador > 1:
            print(f'{contador}', end=' x ')
        else:
            print(f'{contador}',end=f' = {f}\n')
        contador -= 1
    sleep(2)
while True:
    consultar = fatorial()
    consultar = str(input('Quer consultar novamente?(S/N): '))
    print('Processando...')
    sleep(2.5)
    while consultar not in ['S', 's', 'n', 'N']:
        print('Não compreendi, TENTE NOVAMENTE...')
        sleep(2)
        consultar = str(input('Quer consultar novamente?(S/N): '))
        print('Processando...')
        sleep(2.5)
    if consultar in ['S','s']:
        pass
    elif consultar in ['n', 'N']:
        break
    else:
        break
print('FIM DO PROGRAMA...')
