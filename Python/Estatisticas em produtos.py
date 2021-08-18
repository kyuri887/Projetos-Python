from time import sleep

cont = tot = mil = menor = 0
barato = ''

while True:
    print('-=-' * 10)
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço do produto: '))
    cont += 1
    tot += preço
    if preço > 1000:
        mil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else: 
        if preço < menor:
            menor = preço
            barato = produto
    continuar = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    while continuar not in ['S', 'N']:
        print('-=-'*10)
        print('Comando errado, TENTE NOVAMENTE!')
        sleep(2)
        continuar = str(input('Quer continuar?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if continuar in ['N']:
        break
print(f'Total da compra foi de R${tot:.2f}')
sleep(2)
print(f'{mil} produto/s custa mais de R$1000.00')
sleep(2)
print(f'O preço do menor produto é igual R${menor:.2f}, e se chama {barato}')