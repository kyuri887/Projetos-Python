import colorama as color
from time import sleep as sp
color.init()

def primo():
    n1 = int(input('Digite um número: '))
    print('PROCESSING...')
    sp(2)
    tot = 0
    for c in range(1, n1 + 1):
        if n1 % c == 0:
            print('\033[31m', end = ' ')
            tot+=1
        else:
            print('\033[33m', end = ' ')
        print(f'{c}', end = ' ')
    print(f'\n\033[mO número {n1} foi divisivel {tot} vezes')
    if tot == 2:
        print('Por isso é um número Primo!')
    else:
        print('Por isso não um número Primo!')
while True:
    return_for_me = primo()
    return_for_me = str(input('Quer consultar novamente? '))
    if return_for_me in ['Sim', 'sim', 'SIM']:
        pass
    elif return_for_me in ['não', 'Não', 'nao', 'NÃO', 'NAO', 'Nao']:
        break
    else:
        break



