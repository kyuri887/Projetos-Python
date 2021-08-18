from time import sleep

maior18 = masculino = fem20 = 0
while True:
    print('-=-' * 10)
    print('CADASTRE UMA PESSOA!')
    print('-=-' * 10)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    sexo = str(input('Sexo(M/F): ')).upper().strip()
    while sexo not in ['M','F']:
        print('Acredito que você digitou errado, TENTE NOVAMENTE!')
        sleep(2)
        sexo = str(input('Sexo(M/F): ')).upper().strip()
        print('Processando...')
        sleep(2)
    if sexo in ['M']:
        masculino += 1
    if sexo in ['F'] and idade <= 20:
        fem20 += 1
    continuar = str(input('Quer continuar?(S/N): ')).upper().strip()
    while continuar not in ['S', 'N']:
        print('Acredito que você digitou errado, TENTE NOVAMENTE!')
        sleep(2)
        continuar = str(input('Quer continuar?(S/N): ')).upper().strip()
    if continuar in ['N']:
        break
print(f'Tem {maior18} pessoa/s maior de 18 anos;')
sleep(2)
print(f'Tem {masculino} homem/ns;')
sleep(2)
print(f'E tem {fem20} mulher/es menor de 20 anos!')