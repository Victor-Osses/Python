n1 = int(input('\033[1mInforme um número inteiro qualquer:\033[m '))
n2 = int(input('\033[1mInforme um outro número inteiro qualquer:\033[m '))

if n1 > n2:
    print( '\033[31mO primeiro valor é maior que o segundo!!!\033[m')
elif n2 > n1:
    print('\033[32mO segundo valor é maior que o primeiro!!!\033[m')
else:
    print('\033[33mOs dois valores são iguais!!!\033[m')
