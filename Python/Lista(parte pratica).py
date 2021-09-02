from time import sleep

def big_small():
    valores = list()

    for v in range(0, 5):
        valores.append(int(input(f'Digite o {v+1}º valor: ')))
    print('Processing...')
    sleep(2)

    print('='* 100 )
    print(f'Você digitou os valores {valores}')
    sleep(2)
    print(f'O maior valor é o {max(valores)} e está na posição ', end='')

    for i, v in enumerate(valores):

        if v == max(valores):
            print(f'{i+1}...', end='')

    print('end')
    sleep(2)
    print(f'O menor valor é o {min(valores)} e está na posição ', end='')

    for i, v in enumerate(valores):

        if v == min(valores):
            print(f'{i+1}...', end='')
    print('end')
while True:
    retorno = big_small()
    retorno = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(3)
    while retorno not in ['S','N']:
        print('Valor inválido, Tente novamente...')
        sleep(2)
        retorno = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(3)
    if retorno in ['S']:
        pass
    elif retorno in ['N']:
        break
    else:
        break
print('Fim do programa!')