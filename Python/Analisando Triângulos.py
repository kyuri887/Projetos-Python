r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
n1 = r1 == r2 == r3
n2 = r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end = '')
    if n1:
        print('Equilátero!')
    elif n2:
        print('Isóceles!')
    else:
        print('Escaleno!')
else: 
    print('Os segmentos acima não podem formar um triângulo!')

