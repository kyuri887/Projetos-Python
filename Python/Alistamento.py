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
            print(f'Você deveria ter se alistado há \033[35m{soma}\033[m anos atrás!')
            alistamento = ano_atual - soma
            print(f'Seu alistamento foi em \033[34m{alistamento}\033[m!')
        elif idade < 18:
            soma = 18 - idade
            print(f'Você deve se alistar daqui há \033[35m{soma}\033[m anos!')
            alistamento = ano_atual + soma
            print(f'Seu alistamento será em \033[34m{alistamento}\033[m!')
        else:
            print('Você deve se alistar \033[31mIMEDIATAMENTE!\033[m')
    elif sexo == 2:
            print('\033[33mVocê não precisa se alistar para o serviço militar!\033[m')

while True:
    
    consultar = alistamento_militar()
    
    consultar = str(input('Você quer consultar novamente?(S/N) ')).upper().strip()[0]
    
    while consultar not in ['S', 's', 'N', 'n']:
        print('Valor não compreendido, TENTE NOVAMENTE!')
        consultar = str(input('Quer consultar novamente?(S/N) '))
    
    if consultar in ['S', 's', 'Sim', 'SIM','sim']:
        pass
    elif consultar in ['nao', 'Não', 'NÃO','não','Nao', 'NAO', 'n', 'N']:
        break
    else:
        break




