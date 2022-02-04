from time import sleep
opção = 0
n1 = int(input('Informe um número inteiro qualquer: '))
n2 = int(input('Informe outro número inteiro qualquer: '))

while opção != 5:
    print('=-'*30)

    opção = int(input("""
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa:
"""))

    if opção == 1:
        print('{} + {} = {}' .format(n1, n2, n1 + n2))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} é igual a {}'.format(n1, n2))
    elif opção == 4:
        n1 = float(input('Informe um número qualquer: '))
        n2 = float(input('Informe outro número qualquer: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida!!!')
print('=-' * 30)
