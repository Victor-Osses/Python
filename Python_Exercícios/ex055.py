nomeHomem = ''
idadeHomem = 0
média = 0
soma = 0
mulheresMenor20 = 0

for count in range(1, 5):
    print('-'*12, '{} pessoa' .format(count), '-'*12)
    nome = str(input('Informe seu nome completo: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade

    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            if count == 1:
                nomeHomem = nome
                idadeHomem = idade
            elif idade >= idadeHomem:
                    idadeHomem = idade
                    nomeHomem = nome
        else:
            if idade < 20:
                mulheresMenor20 += 1

print('\nA média do grupo é {:.2f}' .format(soma / 4))
print('O homem mais velho do grupo se chama {}. Ele tem {} anos' .format(nomeHomem, idadeHomem))
print('O número de mulheres com menos de 20 anos no grupo é {}' .format(mulheresMenor20))