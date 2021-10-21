from time import sleep

ficha = list()
while True:
    nome = str(input('Nome: ')).upper().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1 + nota2)/2
    ficha.append([nome, [nota1,nota2], m])
    c = str(input('Quer continuar?[S/N]: ')).upper().strip()
    print('Processando...')
    sleep(2)
    print('-=' * 30)
    while c not in ['S', 'N']:
        print('Resposta inválida!')
        sleep(1.5)
        c = str(input('Quer continuar?[S/N]: ')).upper().strip()
        print('Processando...')
        sleep(2)
        print('-=' * 30)
    if c in ['S']:
        pass
    elif c in ['N']:
        break
print(f'{"Nº":<4}{"Nome/s":<10}{"Média":>8}')
print('-=' * 15)
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno?[999 para encerrar]: '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'As notas do {ficha[opc][0]} foi {ficha[opc][1]}')