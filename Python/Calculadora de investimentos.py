from time import sleep
import colorama as color
color.init()

def ROE():
    capital = int(input('Capital investido: '))
    lucro_liquido = int(input('Lucro liquido da empresa(12 meses): '))
    patrimonio_liquido = int(input('Patrimonio Liquido da empresa: '))
    print('Processando...')
    sleep(3)
    roe = (lucro_liquido/patrimonio_liquido)*100
    lucro = capital * roe / 100
    print(f'O ROE dessa empresa é de \033[32m{roe:.2f}%\033[m')
    print(f'Isso quer dizer que o investidor irá lucrar \033[32mR${lucro:.2f}\033[m ao ano')
    if roe < 10:
        print('ROE abaixo da média!')
    else:
        print('ROE lucrativo!')

while True:
    consultar = ROE()
    consultar = str(input('Quer consultar o ROE novamente?(S/N): '))
    print('Processando...')
    sleep(2)
    while consultar not in ['s', 'S', 'n', 'N']:
        print('Não compreendi, TENTE NOVAMENTE!')
        sleep(2)
        consultar = str(input('Quer consultar o ROE novamente?(S/N): '))
        print('Processando...')
        sleep(2)
    if consultar in ['S', 's']:
        pass
    elif consultar in ['n', 'N']:
        break
    else:
        break

n = str(input('Digite uma letra: '))
if n[0] in 'aeiou':
    print(n)
