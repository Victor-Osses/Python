count = soma = 0
while True:
    num = int(input('Informe um número inteiro qualquer: '))
    if num != 999:
        count += 1
        soma += num
    else:
        print(f'\nA soma entre os {count} números informados é igual a {soma}')
        break
