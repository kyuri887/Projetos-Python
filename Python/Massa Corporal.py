import colorama
from time import sleep

peso = float(input('Qual o seu peso: (Kg)'))
altura = float(input('Qual a sua altura: '))
massa_corporal = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de \033[33m{massa_corporal:.1f}\033[m')
if massa_corporal <= 18.5:
    print('\033[35mPeso abaixo da média!\033[m')
elif massa_corporal <= 25:
    print('\033[35mPeso ideal!\033[m')
elif massa_corporal <= 30:
    print('\033[35msobrepeso\033[m')
elif massa_corporal <= 40:
    print('\033[35mObesidade!\033[m')
elif massa_corporal > 40:
    print('\033[35mObesidade Mórbida!\033[m')