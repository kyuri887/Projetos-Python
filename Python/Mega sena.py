from random import randint
from time import sleep

def mega_sena():
    lista = []
    jogos = []
    quant = int(input('Quantas vezes você quer jogar?: '))
    print('-=' * 30)
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        sleep(2)
print('-=' * 30)
while True:
    r = mega_sena()
    r = str(input('Quer consultar novamente?[S/N]: ')).upper().strip()
    print('Processando...')
    sleep(2)
    while r not in ['S','N']:
        print('-=' * 30)
        print('Resposta inválida, Tente Novamente!')
        sleep(1.5)
        r = str(input('Quer consultar Novamente?[S,N]: ')).strip().upper()
        print('Processando...')
        sleep(1.5)
    if r in ['S']:
        pass
    elif r in ['N']:
        break
print('-=' * 30)
print('          Fim do programa        ')
