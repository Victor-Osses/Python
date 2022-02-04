from random import choice, shuffle
al1 = str(input('Primeira aluna: '))
al2 = str(input('Segunda aluna: '))
al3 = str(input('Terceira aluna: '))
al4 = str(input('Quarta aluna: '))

nomes = [al1, al2, al3, al4]
tamanho = len(nomes)

print('Métodos de um array:', dir(nomes), '\n')
cont = 1

#embaralha a lista
shuffle(nomes)
print('Forma 1:', nomes)

print('\nForma 2:\n')
while cont <= tamanho:
    sorteada = choice(nomes)
    nomes.remove(sorteada)
    print('A {}° sorteada foi a {}' .format(cont, sorteada))
    cont = cont + 1

