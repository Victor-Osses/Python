#import math
import emoji
from math import sqrt
import random as rand

num = float(input('Digite um número: '))
raiz = sqrt(num)
#raiz = math.sqrt(num)


#math.ceil arredonda para cima
#math.floor arredonda para baixo
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))
print('Número gerado aleatóriamente pelo computador: {}'.format(rand.random()))
print('Número inteiro delimitado por um intervalo que é gerado aleatóriamente pelo computador: {}'.format(rand.randint(1, 10)))
print(emoji.emojize('Olá, mundo :kissing_heart:', use_aliases=True))

