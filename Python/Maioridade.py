from time import sleep
import colorama as color
from datetime import date
color.init()

def maioridade():

    totmaior = 0
    totmenor = 0
    cont = 0
    for maior in range(1, 8):
        ano = int(input(f'Em que ano a {maior}ª pessoa nasceu?: '))
        data = date.today().year
        idade = data - ano
        cont += 1
        if idade >= 21:
            totmaior += 1
        else:
            totmenor += 1
    print('Processing...')
    sleep(3)
    print(f'{totmaior} dos {cont} são maiores de idade!')
    sleep(4)
    print(f'{totmenor} dos {cont} são menores de idade!')
    sleep(4)

while True: 
     
    retorno = maioridade()
    print('''\033[33mQuer consultarar novamente?\033[m
    \033[32m[ 1 ]Sim\033[m
    \033[31m[ 2 ]Não\033[m''')
    retorno = int(input('Escolha uma opção?(\033[32m1\033[m/\033[31m2\033[m): '))
    print('Processing...')
    sleep(4)
    if retorno == 1:
        pass
    elif retorno == 2:
        break
    elif retorno != 1 and retorno != 2:
        print('Opção invalida, TENTE NOVAMENTE!')
    else:
        break
