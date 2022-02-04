número = int(input('Informe um número inteiro para descobrir seu fatorial: '))
fatorial = número
count = número - 1

if número != 0:
    while count >= 1:
        fatorial *= count
        count -= 1
else:
    fatorial = 1
print('O fatorial de {} é igual a {}' .format(número, fatorial))