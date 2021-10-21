from time import sleep

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
colthree = 0
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para matriz{l, c}: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    colthree += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print('-='*30)
print(f'A soma de todos os números pares é igual a {somap}')
print(f'A soma dos números da coluna 3 é igual a {colthree}')
print(f'O maior valor da linha 2 é igual a {mai}')