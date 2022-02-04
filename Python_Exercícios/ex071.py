times = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians', 'Flamengo', 'Atlético Mineiro', 'Athletico Paranaense',
         'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Banhia', 'Sport', 'Vitória',
         'Ponte Preta', 'América', 'Coritiba')

print('Ranking da CBF para 2019')
print(f'\033[1mOs 5 primeiros colocados:\n\033[m{times[:5]}')
print('-' * 70)

print('\033[1m4 últimos colocados:\033[m')
for pos in range(16, 20):
    print(f'{pos + 1}° {times[pos]}')
print('-' * 70)

print(f'\033[1mTimes em ordem alfabética:\033[m\n{sorted(times)}')
print('-' * 70)

print(f'O Chapecoence está na {times.index("Chapecoense") + 1}° posição')
