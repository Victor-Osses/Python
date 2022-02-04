from random import randint
from time import sleep

acertou = False
palpites = 0
n1 = randint(0, 5)

while not acertou:
    print('-=-'*27)
    n2 = int(input('Vou pensar em um número entre 0 e 5. Tente adivinhar qual número eu escolhi! '))
    print('-=-'*27)
    palpites += 1
    print('PROCESSANDO...')
    sleep(.8)
    if n1 == n2:
        print('\033[32mVocê acertou com {} palpites!!! Eu realmente pensei no número {}\033[m' .format(palpites, n1))
        acertou = True
    elif n2 > n1:
        print('\033[31mHmmm, eu tava pensando em um valor mais baixo... Tenta de novo aí!!!\033[m\n\n')
    elif n2 < n1:
        print('\033[31mHmmm, eu tava pensando em um valor mais alto... Tenta de novo aí!!!\033[m\n\n')
    else:
        print('\033[31m\nVocê errou!!! Talvez na próxima...\033[m')
