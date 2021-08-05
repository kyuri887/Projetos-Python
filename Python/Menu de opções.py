from time import sleep
import colorama as color
color.init()

opções = 0
while opções != 7: 
    print('-=-'*7)
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    print('Processando...')
    sleep(3)
    print('-=-'*7) 
    print('''[ 1 ]Somar
[ 2 ]Subtrair
[ 3 ]Multiplicar
[ 4 ]Dividir
[ 5 ]Maior
[ 6 ]Novos números
[ 7 ]Sair do programa
''')
    opções = int(input('Escolha uma opção: '))
    print('Processando...')
    sleep(3)

    if opções == 1:
        print(f'A soma de {valor1} + {valor2} é igual a {valor1 + valor2}')
        sleep(2)
        consultar = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)

        while consultar not in ['S', 's', 'N', 'n']:
            print('Valor inválido, TENTE NOVAMENTE!: ')
            sleep(2)
            consultar = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
            print('Processando...')
            sleep(2)
    
        if consultar in ['S', 's']:
            opções
        elif consultar in ['N', 'n']:
            break
        else:
            break

    elif opções == 2:
        print(f'A subtração de {valor1} - {valor2} é igual a {valor1-valor2}')
        sleep(2)
        consultar3 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(3)
    
        while consultar3 not in ['S', 'N', 's', 'n']:
            print('Valor inválido, TENTE NOVAMENTE!')
            sleep(2)
            consultar3 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
            print('Processando...')
            sleep(3)
        if consultar3 in ['S', 's']:
            opções
        elif consultar3 in ['N', 'n']:
            break
        else:
            break

    elif opções == 3:
        print(f'A multiplicação de {valor1} x {valor2} é igual a {valor1 * valor2}')
        sleep(2)
        consultar1 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
    
        while consultar1 not in ['S', 's', 'N','n']:
            print('Valor inválido, TENTE NOVAMENTE!')
            sleep(2)
            consultar1 = str(input('Quer consultar novamente?(S/N): '))
            print('processando...')
            sleep(2)
    
        if consultar1 in ['S', 's']:
            opções
        elif consultar1 in ['N', 'n']:
            break
        else:
            break

    elif opções == 4:
        print(f'A divisão de {valor1} / {valor2} é igual a {valor1 / valor2}')
        sleep(2)
        consultar4 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(3)
        while consultar4 not in ['S', 's', 'N', 'n']:
            print('Valor inválido, TENTE NOVAMENTE!')
            sleep(2)
            consultar4 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
            print('Processando...')
            sleep(3)
        if consultar4 in ['S','s']:
            opções
        elif consultar4 in ['n', 'N']:
            break
        else:
            break

    elif opções == 5:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor é {valor2}')
        else:
            print('Os dois valores são iguais!')
        consultar2 = str(input('Quer consultar novamente?(S/N): ')).upper().strip()
        print('Processando...')
        sleep(2)
    
        while consultar2 not in ['S', 'N', 's', 'n']:
            print('Valor inválido, TENTE NOVAMENTE!')
            sleep(2)
            consultar2 = str(input('Quer consultar novamente?(S/N): '))
            print('Processando...')
            sleep(2)
    
        if consultar2 in ['S', 's']:
            opções
        elif consultar2 in ['N', 'n']:
            break
        else:
            break

    elif opções == 6:
        print('Digite novamente...')
        sleep(2)
        print('aguarde..')
        sleep(3.5)
        opções

    elif opções == 7:
        break
    else:
        print('Valor inválido, TENTE NOVAMENTE!')
        sleep(2)
        opções

print('----------Fim do programa, volte sempre!----------')
sleep(5)


    


        
        
     

        
    
    
    
    
    
