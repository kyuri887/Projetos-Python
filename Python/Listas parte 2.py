from time import sleep as sp

def galera():
    dados = list()
    lista = list()
    totmaior = totmenor = 0
    for p in range(0,5):
        dados.append(str(input(f'Nome da {p+1}ª pessoa: ')))
        dados.append(int(input(f'idade da {p+1}ª pessoa: ')))
        print('-=' * 20)
        lista.append(dados[:])
        dados.clear()
    for dado in lista:
        if dado[1] >= 18:
            print(f'{dado[0]} é maior de 18 anos!')
            totmaior += 1
        else:
            print(f'{dado[0]} é menor de idade!')
            totmenor += 1
    print('-=' * 20)
    print(f'Ao total tem {totmaior} pessoa/s maiores de idade!')
    sp(2)
    print(f'E {totmenor} pessoa/s menores de idade')
while True:
    c = galera()
    c = str(input('Quer conusltar mais dados?(S/N): ')).upper().strip()
    print('Processando...')
    sp(3)
    while c not in ['S', 'N']:
        print('Não compreendi, Tente Novamente')
        sp(2)
        c = str(input('Quer consultar mais dados?(S/N): ')).upper().strip()
        print('Processando...')
        sp(2)
    if c in ['S']:
        pass
    elif c in ['N']:
        break
    else:
        break
print('-=' * 20)
print('Fim do Programa')
