vogais = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 
'Praticar', 'Trabalhar', 'Mercado', 'Programador')
for c in range(0, len(vogais)):
    print(f'\nNa palavra {vogais[c].upper()} temos: ', end=' ')
    for letra in vogais[c]:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end= ' ')