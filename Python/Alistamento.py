import colorama
import time
from datetime import date
colorama.init()
def alistamento_militar():
    sexo = int(input('''Qual o seu sexo?
    [1]Masculino
    [2]Feminino
    Opção: '''))
    print('Processing...')
    time.sleep(2)
    if sexo == 1:
        ano = int(input('Ano de nascimento: '))
        ano_atual = date.today().year
        idade = ano_atual - ano
        print('Processing...')
        time.sleep(2)
        if idade > 18:
            soma = idade - 18
            print(f'Você deveria ter se alistado a {soma} anos atrás!')
            alistamento = ano_atual - soma
            print(f'Seu alistamento foi em {alistamento}!')
        elif idade < 18:
            soma = 18 - idade
            print(f'Você deve se alistar daqui há {soma} anos!')
            alistamento = ano_atual + soma
            print(f'Seu alistamento será em {alistamento}!')
        else:
            print('Você deve se alistar IMEDIATAMENTE!')
    elif sexo == 2:
            print('Você não precisa se alistar para o serviço militar!')

while True:
    
    consultar = alistamento_militar()
    
    consultar = str(input('Você quer consultar novamente? '))
    if consultar in ['nao', 'não', 'Não','Nao', 'NÃO','NAO']:
        break
    elif consultar in ['sim','Sim','SIM']:
        pass
    else:
        print('Valor não compreendido, TENTE NOVAMENTE!')
        pass
    



