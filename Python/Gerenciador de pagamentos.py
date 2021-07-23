import time
import colorama
def gerenciador_de_pagamento():
    preço = float(str(input('Preço das compras: R$')))
    print('''Escolha de pagamento:
    [ 1 ]A vista dinheiro/cheque: 10% de desconto.
    [ 2 ]A vista no cartão: 5% de desconto.
    [ 3 ]Em até duas 2x no cartão: preço formal.
    [ 4 ]3x ou mais no cartão: 20% de juros.''')
    opção = int(input('Opção de pagamento: '))
    print('processando...')
    time.sleep(2)
    if opção == 1:
        print('Você ganhará 10% de desconto!')
        print(f'Sendo assim as compras custaram R${preço - (preço * 10 / 100 ):.2f}.')
    elif opção == 2:
        print('Você ganhará 5% de desconto!')
        print(f'Sendo assim as compras custaram R${preço - (preço * 5 /100):.2f}')
    elif opção == 3:
        print(f'As compras sairam em 2x de R${preço / 2:.2f}.')
        print(f'Sendo assim custando o preço formal de R${preço:.2f} no final.')
    elif opção == 4:
        parcelas = int(input('Quantas parcelas: '))
        if parcelas >= 3:
            print(f'Compras com 20% de juros')
            print(f'As compras sairam em {parcelas}x de R${(preço + (preço * 20 / 100)) / parcelas:.2f}')
            print(f'Sendo assim as compras custaram R${preço + (preço * 20 / 100):.2f} no final.')
        else:
            print('Parcela não compreendida, TENTE NOVAMENTE...')
    else:
        print('Valor não compreendido, TENTE NOVAMENTE...') 
while True:
    consulta = gerenciador_de_pagamento()
    consulta = str(input('Quer consultar novamente? '))
    if consulta in ['sim', 'Sim', 'SIM']:
        pass
    elif consulta in ['não', 'nao','Não', 'Nao', 'NAO','NÃO']:
        break
    else:
        break


