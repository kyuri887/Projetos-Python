from time import sleep

pessoas = dict()
dados = list()
listai = list()
media = mediaid = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo(M/F): ')).upper().strip()
    while sexo not in ['M', 'F']:
        print('Erro: por favor digite [M] ou [F]!')
        sleep(2)
        sexo = str(input('Sexo(M/F): ')).upper().strip()
    pessoas['Sexo'] = sexo
    pessoas['Idade'] = int(input('Idade: '))
    listai.append(pessoas['Idade'])
    dados.append(pessoas.copy())
    resp = str(input('Quer continuar?(S/N): ')).upper().strip()
    print('Processando...')
    print('-=' * 30)
    sleep(2)
    while resp not in ['S', 'N']:
        print('Erro: por favor digite [S] ou [N]')
        sleep(2)
        resp = str(input('Quer continuar?(S/N): ')).strip().upper()
        print('Processando...')
        sleep(2)
        print('-=' * 30)
    if resp in ['S']:
        pass
    elif resp in ['N']:
        break
cont = 0
for i in dados:
    cont += 1
print(f'A) Ao todo foram cadastrado {cont} Pessoas')
media = sum(listai)
mediaid = media / cont
print(f'B) A média de idade é de {mediaid} anos')
fem = 0
print(f'C) As mulheres cadastradas foram', end=' ')
for fem in dados:
    if fem['Sexo'] in ['F']:
        print(f'{fem["Nome"]}', end=' ')
print()
print('D) As pessoas acima da média de idades são: ')
for p in dados:
    if p['Idade'] > mediaid:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('>>> ENCERRADO <<<')

