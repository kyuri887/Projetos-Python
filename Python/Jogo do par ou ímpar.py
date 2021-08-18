from time import sleep
from random import randint
import colorama as color

color.init()

def P_I():

    jogador = 0

    while True:
        
        computador = randint(0, 10)
        
        n = int(input('\033[34mDigite um valor de (0 a 10):\033[m '))
        
        while n > 10 or n < 0:
            
            print('Você pode apenas escolher um número entre 0 e 10!')
            sleep(2)
            
            print('TENTE NOVAMENTE...')
            sleep(2)
            
            n = int(input('\033[34mDigite um valor de (0 a 10):\033[m '))
        
        print('Processando...')
        sleep(2.5)

        print('-=-' * 10)
        print('''\033[35m[ 1 ] PAR\033[m  \033[36m[ 2 ] ÍMPAR\033[m''')
        print('-=-' * 10)

        opção = int(input('\033[34mEscolha uma opção:\033[m '))
        print('Processando...')
        sleep(2) 

        while opção not in [1, 2]:
           
            print('Escolha inválida!')
            sleep(1.5)

            print('TENTE NOVAMENTE...')
            sleep(2)
            
            print('-=-' * 10)
            print('''\033[35m[ 1 ] PAR\033[m  \033[36m[ 2 ] ÍMPAR\033[m''')
            print('-=-' * 10)

            opção = int(input('Escolha uma opção: '))

            print('Processando...')
            sleep(2)

        soma = n + computador

        if opção == 1 and soma % 2 == 0:
            jogador += 1
            print('-=-' * 10)
            print('\033[32mVITÓRIA DO JOGADOR!\033[m')
            sleep(2)
            print(f'Você jogou {n} e o computador jogou {computador}, no total deu {soma} é PAR!')
            sleep(3)
            print('Vamos jogar novamente...')
            print('-=-' * 10)
            sleep(2)

        elif opção == 1 and soma % 2 != 0:
            print('-=-' * 10)
            print('\033[33mVITÓRIA DO COMPUTADOR!\033[m')
            sleep(2)
            print(f'Você jogou {n} e o computador jogou {computador}, no total deu {soma} é ÍMPAR!')
            sleep(3)
            break

        elif opção == 2 and soma % 2 != 0:
            jogador += 1
            print('-=-' * 10)
            print('\033[32mVITÓRIA DO JOGADOR!\033[m')
            sleep(2)
            print(f'Você jogou {n} e o computador jogou {computador}, no total deu {soma} é ÍMPAR!')
            sleep(3)   
            print('Vamos jogar novamente...')
            print('-=-' * 10)
            sleep(2)

        elif opção == 2 and soma % 2 == 0:
            print('-=-' * 10)
            print('\033[33mVITÓRIA DO COMPUTADOR!\033[m')
            sleep(2)
            print(f'Você jogou {n} e o computador jogou {computador}, no total deu {soma} é PAR!')
            sleep(3)
            break

    print('-=-' * 10)
    print('\033[31mGAME OVER!\033[m')

    if jogador == 1:
        print('\033[32mVocê venceu uma vez!\033[m')
        print('-=-' * 10)
    else:
        print(f'\033[32mVocê venceu {jogador} vezes!\033[m')
        print('-=-' * 10)

while True:

    jogar_novamente = P_I()

    jogar_novamente = str(input('\033[33mQuer jogar novamente?(S/N):\033[m ')).upper().strip()
    print('Processando...')
    sleep(2.5)
    while jogar_novamente not in ['S', 's', 'n', 'N']:
        print('Valor digitado inválido, TENTE NOVAMENTE!')
        sleep(2)
        jogar_novamente = str(input('\033[33mQuer jogar novamente?(S/N):\033[m ')).upper().strip()
        print('Processando...')
        sleep(2)
    
    if jogar_novamente in ['s', 'S']:
        pass
    elif jogar_novamente in ['n', 'N']:
        break
    else:
        break
print('-=-' * 10)

print('\033[32mFIM do programa, VOLTE SEMPRE!\033[m')
    