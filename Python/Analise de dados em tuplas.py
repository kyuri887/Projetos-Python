from time import sleep

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), 
int(input('Digite um ultimo número: ')))
print('Processando...')
sleep(3)
print(f'Você digitou os números {num}')
print(f'Você digitou o número 9, {num.count(9)} vezes')
print(f'O número 3 está na {num.index(3)+1}ª posição')
print('O números pares são ', end='' )
for n in num:
    if n % 2 == 0:
        print(n, end=' ')