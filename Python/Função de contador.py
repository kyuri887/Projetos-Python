from time import sleep

def linha():
    print('-=' * 30)

def contador(i, f, p):
    if p < 0:
        p*= -1

    if i <= f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(1)
            cont -= p 
        print('FIM')       

contador(0, 10, 2)
linha()
contador(10, 0, 2)
linha()
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)
