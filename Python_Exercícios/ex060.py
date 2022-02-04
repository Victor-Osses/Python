count = 1
mais = 1
qtdTermos = 0
primeroTermo = int(input('Informe o primeiro termo da PA: '))
razão = int(input('Informe a razão da PA: '))

while mais != 0:
    print('{} ' .format(primeroTermo), end='')
    while count < 10 + qtdTermos:
        print(primeroTermo + count * razão, end=' ')
        count += 1

    mais = int(input("""\nQuantos termos mostrar a mais: """))
    qtdTermos = mais
    count = 1

