continuar = 'S'
maior = menor = count = soma = 0
while continuar == 'S':
    num = int(input('Informe um número inteiro qualquer: '))
    if count == 0:
        maior = num
        menor = num
    elif num >= maior:
        maior = num
    elif num <= menor:
        menor = num
    count += 1
    soma += num
    continuar = str(input('Continuar o programa [ S/N ]: ')).upper().strip()[0]
print('\nA média entre os {} termos digitados é {}' .format(count, soma / count))
print('O maior termo digitado foi o {}' .format(maior))
print('O menor termo digitado foi o {}' .format(menor))
