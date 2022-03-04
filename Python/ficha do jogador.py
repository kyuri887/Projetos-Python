import math

def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols')
    

n = str(input('Nome do jogador: '))
g = str(input('Gols feito pelo jogador na partida: '))

if g.isnumeric():
    g=int(g)

else:
    g=0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
