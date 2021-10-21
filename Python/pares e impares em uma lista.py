#pedir 7 números
from time import sleep

def par_impar():
    num = [[], []]

    for v in range(1, 8):
        n = int(input(f'Digite o {v}º valor: '))
        if n % 2 == 0:
            num[0].append(n)
        elif n % 2 == 1:
            num[1].append(n)
    print(f'Os numéros digitados foram {num}')
    sleep(2)
    print(f'Os números pares são {sorted(num[0])}')
    sleep(2)
    print(f'Os números impares são {sorted(num[1])}')    

while True:
    retorno = par_impar()
    retorno = str(input('Quer colocar mais valores na lista? (S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    while retorno not in ['S', 'N']:
        print('Tente novamente!')
        sleep(2)
        retorno = str(input('Quer colocar mais valores na lista? (S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if retorno in ['S']:
        pass
    elif retorno in ['N']:
        break