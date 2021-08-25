from time import sleep

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
int(input('Digite mais um número: ')), int(input('Digite um ultimo número: ')))
print('Processando...')
sleep(3)
print(f'Os números digitados foram {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O 3 aparece na posição {num.index(3)}ª posição!')
else:
    print('O número 3 não apareceu em nenhum dos números digitados!')
print('O números pares são', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
print('Acabou!')