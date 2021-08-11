from time import sleep

n = int(input('Quantos termos de fibonacci você quer mostrar? '))
termo1 = 0
termo2 = 1
cont = 3
print(f'{termo1} - {termo2}', end=' - ')
while cont <= n:
    termo3 = termo2 + termo1
    print(termo3, end=' - ')
    termo1 = termo2
    termo2 = termo3 
    cont += 1 
print('FIM')
