n1 = int(input('Informe um número inteiro qualquer: '))
cont = 0

print('\nTabuada do {}\n' .format(n1))

while cont <= 10:
    print('{} x {} = {}' .format(n1, cont, n1*cont))
    cont = cont + 1
