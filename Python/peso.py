from time import sleep
import colorama as color
color.init()

def kg():
    maior = 0
    menor = 0
    for c in range(1, 6):
        peso = float(input(f'Quantos Kg tem a {c}ª pessoa: Kg'))
        if c == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print('Processing...')
    sleep(3)
    print(f'O maior peso da lista é \033[32m{maior}\033[mKg')
    print(f'E o menor peso da lista é \033[31m{menor}Kg')
    sleep(3.5)

while True:
    
    retorno = kg()

    retorno = str(input('\033[32mQuer consultar novamente?\033[m '))
    if retorno in ['Sim', 'SIM', 'sim']:
        pass
    elif retorno in ['Não', 'NÃO', 'não', 'Nao', 'NAO','nao']:
        break
    else:
        break

