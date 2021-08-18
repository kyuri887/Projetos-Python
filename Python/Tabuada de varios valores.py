from time import sleep

c = 0
while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    print('Processando...')
    sleep(2.5)
    if n < 0: 
        break
    print('-=-'*15)
    while c <= 10:
        c+=1
        print(f'{n} X {c:^2} = {n*c}')
        sleep(1)
        if c == 10:
            break
    print('-=-'*15)
    c = 0
print('Fim do programa de tabuada, Volte Sempre!')