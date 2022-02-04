n1 = int(input('\033[1mInforme um número inteiro qualquer:\033[m '))
opções = str(input(
'''\033[1m\nEscolha uma das opções de conversão abaixo:\033[m

\033[32m[ 1 ] - binário\033[m
\033[33m[ 2 ] - octal\033[m
\033[34m[ 3 ] - hexadecimal\033[m
'''))

#Os 2 primeiros caractéres indicam a base do número
if opções == '1':
    print(bin(n1)[2:])
elif opções == '2':
    print(oct(n1)[2:])
elif opções == '3':
    print(hex(n1)[2:])
else:
    print('\033[31mInforme uma opção válida!\033[m')
