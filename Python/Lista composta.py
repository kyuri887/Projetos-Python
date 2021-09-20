from time import sleep as sp
import pandas as pd
import colorama
colorama.init()

dados = list()
lista = list()
mai = men = cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    cont += 1
    if cont == 1:
        mai = dados[1]
        men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1] 
    lista.append(dados[:])
    dados.clear()
    c = str(input('Quer continuar? (S/N): ')).upper().strip()
    while c not in ['S', 'N']:
        print('Tente Novamente, não compreendi!')
        sp(2)
        c = str(input('Quer continuar? (S/N): ')).upper().strip()
    if c in ['S']:
        pass
    elif c in ['N']:
        break
print('Processando...')
sp(2)
print('-=' * 30)
dados_fm = pd.DataFrame(lista)
print(dados_fm)
sp(2)
print(f'Ao todo foram cadastrado {len(lista)} pessoa/s.')
sp(2)
print(f'O maior peso foi {mai}Kg.')
sp(2)
print('Lista dos maiores pesos:')
print('-=' * 30)
for p in lista:
    if p[1] == mai:
        print(f'\033[32m{p[0]}\033[m')
print('-=' * 30)
sp(2)
print(f'E o menor peso foi {men}Kg.')
sp(2)
print('Lista dos menores pesos:')
print('-=' * 30)
for p in lista:
    if p[1] == men:
        print(f'\033[33m{p[0]}\033[m')