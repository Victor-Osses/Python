números = (int(input('Digite um valor inteiro qualquer: ')), int(input('Digite novamente um valor inteiro qualquer: ')), int(input('Digite novamente um valor inteiro qualquer: ')), int(input('Digite novamente um valor inteiro qualquer: ')))
print('\nVocê digitou ', end='')

for n in números:
    print(f'{n} ', end='')

print(f'\nO valor 9 apareceu {números.count(9)} vezes')

if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end='')
for n in números:
    if n % 2 == 0:
        print(f'{n} ', end='')
print('')
