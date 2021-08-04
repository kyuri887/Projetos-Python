import colorama as color
from time import sleep
color.init()

def analisador():
    fem = 0
    media = 0
    mais_velho_do_grupo = 0
    nome_do_mais_velho = ''
    for analisador_completo in range(1, 5):
        print('\033[33mANALISADOR COMPLETO\033[m')
        nome = str(input(f'Nome da {analisador_completo}ª pessoa: ')).upper()
        idade = int(input(f'Idade da {analisador_completo}ª pessoa: '))
        sexo = str(input(f'Sexo da {analisador_completo}ª pessoa(M/F): '))
        print('-=-'*10)
        media += idade
        if analisador_completo == 1 and sexo in ['M', 'm']:
            mais_velho_do_grupo = idade
            nome_do_mais_velho = nome
        elif idade > mais_velho_do_grupo and sexo in ['M', 'm']:
            mais_velho_do_grupo = idade
            nome_do_mais_velho = nome
        if idade < 20 and sexo in ['F', 'f']:
            fem += 1
    print('PROCESSANDO...')
    sleep(4)
    print(f'A média de idade do grupo é de \033[32m{media/4}\033[m ano/s')
    sleep(3.5)
    print(f'O homem mais velho do grupo tem \033[35m{mais_velho_do_grupo}\033[m ano/s e se chama \033[35m{nome_do_mais_velho}\033[m')
    sleep(3.5)
    print(f'No grupo tem \033[31m{fem}\033[m mulher/es com menos de 20 anos')

while True:
    
    retorno = analisador()
    
    retorno = str(input('Quer consultar novamente?(S/N): '))
    print('Processando...')
    sleep(3)
    
    if retorno in ['S', 's']:
        pass
    elif retorno in ['N', 'n']:
        break
    elif retorno != ['S', 's'] and retorno != ['N', 'n']:
        print('\033[31mOPÇÃO NÃO COMPREENDIDA, TENTE NOVAMENTE!\033[m')
        sleep(3)
        print('Aguarde um instante...')
        sleep(4)
        pass
    else:
        break
    
