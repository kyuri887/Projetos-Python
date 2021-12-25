from time import sleep

jogador = {}
lista = list()

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou: '))
cont = 0
while True:
    if partidas != 0:
        lista.append(int(input(f'     Quantos gols o jogador {jogador["Nome"]} fez na {cont+1}ª partida: ')))
        jogador['Gols'] = lista[:]
        jogador['Total'] = sum(lista)
    cont += 1
    if cont == partidas:
        break
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'- O campo {k} tem o valor {v}')
    sleep(1)
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas: ')
for i, v in enumerate(lista):
    print(f' => Na {i+1}ª partida, o jogador {jogador["Nome"]} fez {v} gols!')
    sleep(1)