def area(larg, comp):
    a = larg * comp
    print(f'A área {larg}x{comp} é igual a {a}')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)