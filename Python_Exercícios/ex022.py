n1 = str(input('Informe um número inteiro entre 0 e 9999 '))
casas = ['Unidade', 'Dezena', 'Centena', 'Milhar']
posicao = len(n1) - 1
count = 0

print('Método 1:')

while count <= len(n1) - 1:
    print('{}: {}' .format(casas[count],  n1[posicao]))
    count = count + 1
    posicao = posicao - 1
else:
    while count <= 3:
        print('{}: {}'.format(casas[count], 0))
        count = count + 1

print('\nMétodo 2:')
print('Unidade: {}' .format(int(n1) // 1 % 10))
print('Dezena: {}' .format(int(n1) // 10 % 10))
print('Centena: {}' .format(int(n1) // 100 % 10))
print('Milhar: {}' .format(int(n1) // 1000 % 10))

