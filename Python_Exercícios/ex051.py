número = int(input('Informe um número inteiro qualquer: '))
qtdDiv = 0

for count in range(1, número + 1):
    if número % count == 0:
        qtdDiv += 1
        print('\033[32m{}\033[m' .format(count), end=' ')
    else:
        print('\033[31m{}\033[m' .format(count), end=' ')

print(end='\n')
if qtdDiv == 2:
    print('O número {} é primo!!!' .format(número))
else:
    print('O número {} não é primo!!!'.format(número))
