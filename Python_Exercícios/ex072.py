from random import randint
números = (randint(0, 20), randint(0, 20), randint(0, 20),
           randint(0, 20), randint(0, 20))
print('Números sorteados: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
