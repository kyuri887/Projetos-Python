from random import randint
from time import sleep
import colorama as color
color.init()

def adivinhação():
    nome = 'Kauan'
    computador = randint(0,10)
    
    print(f'Olá \033[36m{nome}\033[m, me chamo \033[36mJarvis\033[m, sou seu assistente virtual!')
    sleep(5)
    print('Neste momento estou pensando em um número entre \033[33m0\033[m e \033[32m10\033[m...')
    sleep(5)
    print('Será que você consegue adivinhar?')
    sleep(5)
    
    acertou = False
    tentativas = 0
    
    while not acertou:
        jogador = int(input('Em que número eu estou pensando...?: '))
        tentativas += 1
        if jogador == computador:
            acertou = True
            sleep(2)
        else:
            if jogador < computador:
                print('Mais um pouco...')
                sleep(2)
            else:
                print('Menos...')
                sleep(2)
    
    if tentativas <= 3:
        print(f'\033[32mNossa que rápido, você acertou em {tentativas} tentativa/s, PARABÉNS!\033[m')
    elif tentativas > 3 and tentativas <= 6:
        print(f'\033[33mPoderia ser melhor, você acertou em {tentativas} tentativas!\033[m')
    else:
        print(f'\033[31mVocê é muito ruim hahahaha, você acertou em {tentativas} tentativas!\033[m')

while True:
    
    repetir = adivinhação()
    repetir = str(input('Quer jogar novamente?(S/N): ')).upper().strip()
    
    while repetir not in ['Sim', 'sim', 'SIM','S', 's', 'n', 'N', 'Não','não','nao','Nao','nao', 'NÃO', 'NAO']:
        print('Valor inválido, \033[31mTENTE NOVAMENTE!\033[m')
        repetir = str(input('Quer jogar novamente?(S/N): ')).upper().strip()
    
    if repetir in ['S', 's', 'Sim', 'SIM','sim']:
        pass
    elif repetir in ['n', 'N', 'Não', 'NÃO','não', 'Nao', 'NAO', 'nao']:
        break
    else:
        break

