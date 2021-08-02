from time import sleep
def tabuada():
    num = int(input('Digite um número para ver sua tabuada: '))
    print('PROCESSANDO...')
    sleep(2)
    for c in range(0, 11):
        print(f'{num} x {c:2} = {num*c}')
while True:
    retorne = tabuada()
    print('''Quer consultar novamente?
    [ 1 ]Sim
    [ 2 ]Não''')
    retorne = int(input('Escolha uma opção: '))
    if retorne == 1:
        pass
    elif retorne == 2:
        break
    else:
        break