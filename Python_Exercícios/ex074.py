produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.90,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 60)
print('{:^60}' .format('LISTAGEM DE PREÇOS'))
print('-' * 60)

for pos in range(0, len(produtos), 2):
    print(f'{produtos[pos]}' + '.' * (40 - len(produtos[pos])), f'R$   {produtos[pos + 1]:>7.2f}')
print('-' * 60)
