from time import sleep

valor = []

while True:
    v = int(input('Digite um valor na sua lista: '))
    
    if v not in valor:
        valor.append(v)
        print('valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    
    c = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    print('-='*20)
    
    while c not in ['S', 'N']:
        print('Não compreendi, TENTE NOVAMENTE!')
        sleep(2)
        c = str(input('Quer continuar?(S/N): ')).upper().strip()
        print('Processando...')
        print('-='*20)
        sleep(2)
    
    if c in ['S']:
        pass
    elif c in ['N']:
        break

print('-='* 20)
print('Os valores da lista são: ')
valor.sort()

for lista in valor:
    print(lista, end='-> ')
print('fim da lista')
