from time import sleep

jogador = dict()
dados = list()
gols = list()
nomes = list()
cont = total = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).upper()
    nomes.append(jogador['Nome'])
    partidas = int(input(f'Quantas Partidas {jogador["Nome"]} jogou: '))
    if partidas != 0:
        cont = 0
        gols.clear()
        while True:
            gols.append(int(input(f'    Quantos gols o {jogador["Nome"]} fez na {cont+1}ª partida: ')))
            total = sum(gols)
            jogador['Gols'] = gols[:]
            jogador['Total'] = total
            cont += 1
            if cont == partidas:
                break
    dados.append(jogador.copy())
    resp = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    print('-=' * 30)
    while resp not in ['S','N']:
        print('Erro: por favor digite [S] ou [N] para prosseguirmos!')
        sleep(2)
        resp = str(input('Quer continuar?(S/N): ')).upper().split()
        if resp == ['S']:
            resp = 'S'
        elif resp == ['N']:
            resp = 'N'
        print('Processando...')
        sleep(2)
        print('-=' * 30)
    if resp in ['S']:
        pass
    elif resp in ['N']:
        break
print()
print('Cod', end=' ')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-=' * 30)
for i, v in enumerate(dados):
    print(f'{i+1:>3}', end= ' ')
    for d in v.values():
        print(f'{str(d):<15}', end='') 
    print()
print('-='*30)     

while True:
    esp = str(input('Quer ver os dados de algum jogador em especifico?(S/N): ')).upper().strip()
    if esp == ['S']:
        esp = 'S'
    print('Processando...')
    sleep(2)
    print('-=' * 30)
    while esp not in ['S', 'N']:
        print(f'Erro: por favor digite (S) ou (N)!')
        sleep(2)
        esp = str(input('Quer ver os dados de algum jogador em especifico?(S/N): ')).upper().strip()
        if esp == ['S']:
            esp = 'S'
        elif esp == ['N']:
            esp = 'N'
        print('Processando...')
        sleep(2)
        print('-=' * 30)
    if esp in ['S']:
        while True:
            qual = str(input('Qual dos jogadores registrados você quer ver os dados?(Digite "stop" para parar): ')).upper().strip()
            if qual == 'STOP':
                break
            if qual in nomes:
                print('-=' * 30)
                print('Cod', end=' ')
                for chave in jogador.keys():
                    print(f'{chave:<15}', end='')
                print()
                print('-=' * 30)
                for p in dados:
                    if qual in p['Nome']:
                        for o in p.values():
                            print(f'{str(o):<17}', end='')
                        print()
            elif qual not in nomes:
                print('Nome não registrado!')
                sleep(2)
                print('Tente novamente!')
                sleep(2)
    elif esp in ['N']:
        break
    break   
print('Fim do programa!')
