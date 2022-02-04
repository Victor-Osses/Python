from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
n1 = randint(0, 5)
n2 = int(input('Informe um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
print('PERDI! Eu pensei no número {} mesmo!' .format(n1) if n1 == n2 else 'GANHEI! Eu pensei no número {} e não no {}!' .format(n1, n2))