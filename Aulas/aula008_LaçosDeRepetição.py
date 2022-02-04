#Laço de Repetição FOR

print('Laço comum:')
for count in range(0, 5):
    print(count)
print('\nLaço pulando de 2 em 2:')
for count in range(1, 11, 2):
    print(count)
print('\nLaço decrescente')
for count in range(10, 0, -1):
    print(count)

i = int(input('\nInício: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for count in range(i, f+1, p):
    print(count)

#Laço de Repetição WHILE
print('\nWHILE:')
c = 1
while c < 10:
    print(c)
    c += 1

c = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#fstrings:
print(f'A soma vale {s:.2f}')
