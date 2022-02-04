print('Soma de todos os ímpares que são múltiplos de três e que se encontram no intervalo entre 1 e 500')
soma = 0
for count in range(3, 501, 3):
    if count % 2 != 0:
        soma += count
print('A soma resultou em {}' .format(soma))