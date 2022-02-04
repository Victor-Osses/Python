soma = 0
for count in range(6, 0, -1):
    valor = int(input('Informe um número inteiro mais {} vezes: ' .format(count)))
    if valor % 2 == 0:
        soma += valor
print('A soma dos valores pares informados resultou em {}' .format(soma))