from time import sleep

def linha():
    print('-=' * 30)


def maior(*num):
    cont = maior = 0
    print('Analisando os valores passado...')
    for valor in num:
        print(valor, end=' ', flush=True)
        cont +=1
        sleep(1)
        if cont == 1:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Foram informado {cont} valores')
    print(f'O maior número informado foi o {maior}')


maior(2, 5, 7, 8, 0)
linha()
maior(7, 6, 2)
linha()
maior(1, 8, 9, 5, 2)
linha()
maior(1, 2)
linha()
maior()
