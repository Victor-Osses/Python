tamanhoSequência = int(input('Informe um número inteiro qualuqer: '))
count = 3
ant1 = 1
ant2 = 0

print('A sequência de fibonnaci com {} termos é a seguinte:\n{} -> {} ->' .format(tamanhoSequência, ant2, ant1), end=' ')
while count <= tamanhoSequência:
    próximo = ant1 + ant2
    print(próximo, end=' -> ')
    ant2 = ant1
    ant1 = próximo
    count += 1
print('FIM')
