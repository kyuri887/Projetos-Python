from datetime import datetime
from time import sleep
dados = dict()

dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
dados['Idade'] = datetime.now().year - nascimento
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário:R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
    sleep(1.5)
