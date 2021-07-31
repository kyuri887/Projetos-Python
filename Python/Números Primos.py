import colorama
colorama.init()

n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[33m', end = ' ')
        tot+=1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ') 
print(f'\n\033[mO numéro {n1} é foi dividido {tot} vezes!')
if tot == 2:
    print('Por isso é um número Primo!')
else:
    print('Por isso não é um número Primo!')