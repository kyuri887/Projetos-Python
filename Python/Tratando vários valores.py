n = int(input('Digite um número[999 para parar]: '))
soma = 0
cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número[999 para parar]: '))
print(f'Você digitou {cont} números e a soma de todos eles é igual a {soma}')