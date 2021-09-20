from time import sleep

lista = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('processando...')
    sleep(2)

    while c not in ['S', 'N']:
        print('Não compreendi, Tente Novamente!')
        sleep(2)
        c = str(input('Quer continuar?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)

    if c in ['N']: 
        break

print('-='*20)
print(f'Os números digitados foram {lista}')
print(f'Ao todo foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Em Ordem decrescente fica {lista}')

if 5 in lista:
    print(f'O número 5 está na lista!')

elif 5 not in lista:
    print('O valor 5 não foi encontrado!')