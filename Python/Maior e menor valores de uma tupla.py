from random import randint
from time import sleep

def sorteios():
    sorteio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    print(f'Os números sorteados são: ', end='')
    for n in sorteio:
        print(n, end=' ')
    print('\n')
    print('='*38)
    print(f'O maior número é {max(sorteio)}')
    print(f'O menor número é {min(sorteio)}')

while True:
    novamente = sorteios()
    novamente = str(input('Quer sortea novamente?(S/N): ')).upper().strip()
    print('processando...')
    sleep(3)
    print('-='*38)
    
    while novamente not in ['S', 'N']:
        print('Escolha não compreendida, TENTE NOVAMENTE!')
        sleep(2)
        novamente = str(input('Quer sortea novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(3)
        print('-='*38)
        
    if novamente in ['S']:
        pass
    elif novamente in ['N']: 
        break
    else:
        break
print('FIM DO SORTEIO!')