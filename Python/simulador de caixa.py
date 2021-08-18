from time import sleep

def banco():
    print('=' * 30)
    print(f"{'BANCO CEV':^30}")
    print('=' * 30)

    valor = int(input('Valor a sacar: R$'))
    total = valor
    cedula = 100
    totcedula = 0
    while True:
        if total >= cedula:
            total -= cedula
            totcedula += 1
        else:
            if totcedula > 0:
                print(f'Total de {totcedula} nota/s de R${cedula}')
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2
            elif cedula == 2:
                cedula = 1
            totcedula = 0
            if total == 0:
                break
while True:
    saque = banco()
    saque = str(input('Quer sacar novamente?(S/N): ')).upper().strip()
    print(f"{'Processando...':^5}")
    sleep(3)
    while saque not in ['S', 'N']:
        print('Valor digitado não compreendido!')
        sleep(2)
        print(f"{'TENTE NOVAMENTE!':^5}")
        sleep(2)
        saque = str(input('Quer sacar novamente?(S/N): ')).upper().strip()
        print(f"{'Processando...':^5}")
        sleep(3)
    if saque in ['N']:
        break
    elif saque in ['S']:
        pass
print(F"{'Saque efetuado com sucesso, VOLTE SEMPRE!':^30}")