from datetime import date
from time import sleep

totmaior = 0
totmenor = 0
cont = 0
for pess in range(1, 8):
    data = date.today().year
    ano = int(input(f'Em que ano a {pess}ª pessoa nasceu?: '))
    idade = data - ano
    cont += 1
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Processing...')
sleep(3)
print(f'De {cont}, {totmaior} são maiores de idade!')
print(f'De {cont}, {totmenor} são menores de idade!')
        
    


        



