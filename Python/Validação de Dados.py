sexo = str(input('Digite o seu sexo(M/F): ')).upper().strip()[0]
while sexo not in ['M', 'm','f', 'F']:
    sexo = str(input('Valor digitado não compreendido.Por favor informe seu sexo: ')).upper().strip()[0]
print(f'Valor {sexo} registrado com sucesso!')


