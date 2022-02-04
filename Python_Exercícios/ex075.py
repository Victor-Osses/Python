palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR',
            'PRÁTICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTÚRO')
for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    for l in p:
        if l.lower() in 'aáãeéiíoóu':
            print(f'{l.lower()} ', end='')
    print('')
