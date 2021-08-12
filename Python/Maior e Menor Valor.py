from time import sleep

n1 = int(input('Digite um número: '))
cont = 1
soma = igual = maior = menor = n1
c = 'S'
while c in ['s', 'S']:
    c = str(input('Quer continuar?(S/N): '))
    if c in ['n', 'N']:
        break
    while c not in ['s', 'S', 'N', 'n']:
        print('valor digitado inválido, TENTE NOVAMENTE...')
        sleep(2)
        c = str(input('Quer continuar?(S/N): ')).upper().strip()
        if c in ['n', 'N']:
            break
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    cont += 1
print(f'A média dos {cont} números inseridos é igual a {soma/cont}')
print(f'E o maior número é o {maior}')
print(f'E o menor número é o {menor}')
