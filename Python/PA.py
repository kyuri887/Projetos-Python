#Termos de uma PA
termo = int(input('Termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    cont += 1
    print(termo, end=' ')
    termo+=razao
print('Fim')