dicionario = dict()
dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input('Média do joão: '))
print('-=' * 30)
print(f'- Nome do aluno é igual a {dicionario["Nome"]}')
print(f'- A média do aluno foi igual a {dicionario["Média"]}')
if dicionario['Média'] >= 7:
    print('- O aluno aprovado!')
elif dicionario['Média'] >= 5 and dicionario['Média'] < 7:
    print('- Aluno está de recuperação!')
else:
    print('- Aluno reprovado')
