from random import randint
from time import sleep
from operator import itemgetter

print('Valores Sorteados:')
jogador = dict()
jogador['Jogador1'] = randint(1, 6)
jogador['Jogador2'] = randint(1, 6)
jogador['Jogador3'] = randint(1, 6)
jogador['Jogador4'] = randint(1, 6)

for k, v in jogador.items():
    print(f'{k} tirou {v} no dado')
    sleep(1.5)
print('-=' * 30)
print('===============RANKING DOS JOGADORES===============')
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1.5)
print('Fim do Programa')