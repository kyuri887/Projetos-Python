import time
import colorama as color
color.init()
def maior_menor():
    maior = 0
    menor = 0
    for c in range(1, 6):
        peso = float(input(f'Qual peso da {c}ª pessoa: Kg '))
        if c == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print('PROCESSING...')
    time.sleep(3)
    print(f'O maior peso é \033[33m{maior}Kg\033[m')
    time.sleep(3)
    print(f'E o menor peso é \033[31m{menor}Kg\033[m')
    time.sleep(3)
while True:
    retorno = maior_menor()
    print('Quer consultar novamente?')
    time.sleep(2)
    print('''Escolha entre a opção 1 e 2:
    \033[32m[ 1 ]Sim\033[m
    \033[31m[ 2 ]Não\033[m''')
    retorno = int(input('Escolha uma das opções acima: '))
    if retorno == 1:
        pass
    elif retorno == 2:
        break
    else:
        break

    
        
    