from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções são:
[ 0 ]Pedra
[ 1 ]Papel
[ 2 ]Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔÔÔ!!!')
print('-=-' * 10)
print(f'O jogador jogou {itens[jogador]}')
print(f'O computador jogou {itens[computador]}')
print('-=-' * 10)
if computador == 0: #pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Vitória do jogador!')
    elif jogador == 2:
        print('Vitória do computador!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #papel
    if jogador == 0:
        print('Vitória do computador!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Vitória do jogador!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('Vitória do jogador!')
    elif jogador == 1:
        print('Vitória do computador!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('JOGADA INVALIDA!')
else:
    print('JOGADA INVALIDA!')