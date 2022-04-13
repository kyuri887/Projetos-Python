def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols!')


n = str(input('Nome do jogador: '))
g = str(input('Saldo de gols do jogador: '))

#Para saber se é um número, e caso seja transformar em um número inteiro!
if g.isnumeric():
    g = int(g)

#Se caso estiver vazio o espaço, g vai receber 0
else:
    g = 0

#se mesmo n limpando todos os espaços ainda estiver vazio, só o gols receberá o g
if n.strip() == '':
    ficha(gols = g)

#Se caso tiver tido algum valor no n, jogador = n e gols = g
else:
    ficha(n, g)
