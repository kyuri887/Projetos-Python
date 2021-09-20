from time import sleep

lista = list()
listap = list()
listai = list() 

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    
    c = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    while c not in ['S', 'N']:
        print('Tente Novamente')
        sleep(2)
        c = str(input('Quer continuar?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if c in ['N']:
        break
print('-=' * 30)
print(f'Os números da lista são {sorted(lista)}')
sleep(2)
print(f'Os números pares da lista são {sorted(listap)}')
sleep(2)
print(f'E os números impares são {sorted(listai)}')