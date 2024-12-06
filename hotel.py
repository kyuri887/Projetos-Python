from time import sleep
from random import randint

cadastro_hotel = [[]]
count = 0

while True:
    while True:
        name_user = str.upper(input('Digite o seu nome: '))
        cpf_user = str.strip(input('Digite o seu cpf: '))

        if len(cpf_user) == 11 and cpf_user.isdigit():
            cadastro_hotel[count].append(name_user)
            cadastro_hotel[count].append(cpf_user)
            break
        else:
            print('Erro, cpf invalido, tente novamente')
            sleep(2)

    hosp_conv = int(input('Quantas pessoas ficaram no quarto: '))
    for c in range(hosp_conv):
        while True:
            name_userc = str.upper(input('Digite o seu nome: '))
            cpf_userc = str.strip(input('Digite o seu cpf: '))
            if len(cpf_userc) == 11 and cpf_userc.isdigit():
                cadastro_hotel[count].append(name_userc)
                cadastro_hotel[count].append(cpf_userc)
                break
            else:
                print('Erro, cpf invalido, tente novamente!')
                sleep(2)
    while True:
        moreone = str.lower(input('Quer fazer mais algum cadastro[y]or[n]: '))
        if moreone == 'y':
            count += 1
            cadastro_hotel.append([])
            break
        elif moreone == 'n':
            break
        else:
            print('Erro, tente novamente!')
    if moreone == 'n':
        break           
print(cadastro_hotel)

