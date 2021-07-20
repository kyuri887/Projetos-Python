import colorama
import time
from datetime import date
colorama.init()
ano = int(input('Ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano
print('Processando...')
time.sleep(2)
print(f'Atleta nascido em {ano} com {idade} anos de idade...')
if idade <= 9:
    print('Classificado como: MIRIM')
elif idade <= 14:
    print('Classificado como: INFANTIL')
elif idade <= 19:
    print('Classificado como: JÚNIOR')
elif idade <= 25:
    print('Classificado como: SÊNIOR')
else:
    print('Classificado como: MASTER')
