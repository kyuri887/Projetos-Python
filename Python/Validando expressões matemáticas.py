from time import sleep

def math():
    n =  str(input('Digite uma expressão: '))
    print('processando...')
    sleep(2)
    pilha = list()
    for simb in n:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    print('-=' * 20)
    if len(pilha) == 0:
        print('Expressão válida!')
        sleep(2)
    else:
        print('Expressão inválida!')
        sleep(2)
while True:
    c = math()
    c = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
    print('Processando...')
    sleep(2)
    while c not in ['S', 'N']:
        print('Não compreendi, tente novamente!')
        sleep(2)
        c = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if c in ['S']:
        pass
    elif c in ['N']:
        break
    else:
        break
print('FIM DO PROGRAMA, VOLTE SEMPRE!')