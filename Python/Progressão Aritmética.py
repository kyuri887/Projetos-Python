print('-=-' * 7)
print('10 TERMOS DE UMA PA')
print('-=-' * 7)
termo = int(input('Termo: '))
Razão = int(input('Razão: '))
cont = termo + (10 - 1) * Razão #formula para calcular a PA
for c in range(termo, cont + Razão, Razão):
    print(c, end = ' ')
print('ACABOU!')

    