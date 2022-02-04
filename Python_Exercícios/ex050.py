p1 = int(input('Informe o primeiro termo da progressão aritimética: '))
razão = int(input('Informe a razão dessa progressão aritimética: '))

pa = '{} -> ' .format(p1)
for count in range(1, 10):
    pa += '{} -> ' .format(count * razão + p1)
print('{}ACABOU' .format(pa))