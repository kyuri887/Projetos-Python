from time import sleep

def numeros():
    cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
    'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
    'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 
    'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 
    'Vinte')
    n = int(input('Digite um número entre 0 a 20: '))
    print('Processando...')
    sleep(3)
    while n > 20: 
        print('Só é aceito números entre 0 a 20!')
        sleep(2)
        print('TENTE NOVAMENTE...')
        sleep(2)
        n = int(input('Digite um número entre 0 a 20: '))
        print('Processando...')
        sleep(3)
    print(f'Você digitou o número {cont[n]}')
    sleep(2)
while True:
    continuar = numeros()
    continuar = str(input('Quer consultar novamente?(S/N):')).upper().strip()
    print('Processando...')
    sleep(2)
    while continuar not in ['S','N']:
        print('Valor não compreendido!')
        sleep(2)
        print('TENTE NOVAMENTE!')
        sleep(2)
        continuar = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if continuar in ['S']:
        pass
    elif continuar in ['N']:
        break
    else:
        break
print('FIM DO PROGRAMA!')