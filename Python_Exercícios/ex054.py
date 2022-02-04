maiorPeso = 0
menorPeso = 0

for count in range(1, 6):
    peso = float(input('Informe seu peso: '))
    if count == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso >= maiorPeso:
            maiorPeso = peso
        elif peso <= menorPeso:
            menorPeso = peso

print('\nO maior peso é {:.2f}Kg' .format(maiorPeso))
print('O menor peso é {:.2f}Kg' .format(menorPeso))