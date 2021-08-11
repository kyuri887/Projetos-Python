termo = int(input('Termo: '))
razão = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end='-')
        termo+=razão
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais quer consultar? '))