from time import sleep

cont = 0
while True:
    print('-=-'*15)
    n = int(input('Digite um número para saber sua tabuada: '))
    print('-=-'*15)
    print('Processando...')
    sleep(2)
    if n < 0:
        break
    while n not in ['-']:
        cont += 1
        if cont > 10:
            cont = 1
        print(f'{n} x {cont:^2} = {n*cont}')
        sleep(1)
        if cont == 10:
            break
print('Fim do programa de tabuada!')