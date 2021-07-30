soma = 0
cont = 0
for c in range(0, 6):
    par = int(input('Digite um número: '))
    if par % 2 == 0:
        soma += par
        cont += 1
print(f'Você informou {cont} números pares e a soma deles é igual a {soma}')
    