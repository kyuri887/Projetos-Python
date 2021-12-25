from time import sleep
from random import randint
from operator import itemgetter

jogador = dict()
jogador['Jogador1'] = randint(1, 6)
jogador['Jogador2'] = randint(1, 6)
jogador['Jogador3'] = randint(1, 6)
jogador['Jogador4'] = randint(1, 6)

print('Valores Jogados:')
for k, v in jogador.items():
    print(f'O jogador {k} tirou {v}')
    sleep(1.5)
print('-='*30)
print('  == Ranking dos jogadores ==  ')
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1),reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} tirou {v[1]}')