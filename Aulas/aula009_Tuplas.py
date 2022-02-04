#Tuplas == Variáveis compostas
#As tuplas são imutáveis!
#Para criar pode-se usar () ou não a partir do python 3.6

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('Posição 1:', lanche[1])
print('Posição -2:', lanche[-2])
print('Posição 1 até a 2:', lanche[1:3])
print('Posição 2 até o final:', lanche[2:])
print('Posição 0 até a posição 1:', lanche[:2])
print('Posição -3 até a posição 3:', lanche[-3:])
#(lache[1] = 'Refrigerante') == error

print('\n')
#for comida in lanche:
#   print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')

#Enumerate() retorna a posição e o valor
for pos, comida in enumerate(lanche):
    print(f'Vou comer o lanche \'{comida}\' na posição {pos}')

print(f'\nEu comi {len(lanche)} lanches')
print(f'Lanches ordenados com sorted(): {sorted(lanche)}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(f'Concatenando tuplas: {c}')
print(f'Quantas vezes aperece o número 5 na tupla c: {c.count(5)}')
print(f'Em que posição está a primeira ocorrência do número 2 na tupla c: {c.index(2)}')
print(f'Em que posição está a primeira ocorrência do número 2 na tupla c a partir da posição 4: {c.index(2, 4)}')

#Uma tupla aceita diferentes tipos de dados simultaneamente
pessoa = ('Victor', 18, 'M', 100.00)
#Apaga uma variável - Não é possível apagar uma posição da tupla, mas da pra apagar ela completamente
del(pessoa)