qtdNúmeros = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n != 999:
        qtdNúmeros += 1
        soma += n
    else:
        break
print(f'A soma desses {qtdNúmeros} valores resultou em {soma}')
