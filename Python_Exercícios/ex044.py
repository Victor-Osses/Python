from random import randint
from time import sleep

clear = '\n' * 50
opções = ['PEDRA', 'PAPEL', 'TESOURA']
style = {'Azul': '\033[34m', 'Clear': '\033[m'}
jogar = 1

while jogar == 1:

    escolhaPc = randint(0, 2)
    escolhaJogador = int(input("""\033[32mJokenpô com o computador.\033[m
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura
\033[35mEscolha sua jogada:\033[m """))

    print('\n\033[31mJO\033[m')
    sleep(1)
    print('\033[32mKEN\033[m')
    sleep(1)
    print('\033[33mPÔ!!!\033[m')
    sleep(0.2)

    print('\n'+'-='*15)
    if escolhaPc + 1 == escolhaJogador:
        print('{}O computador escolehu {}\nO jogador escolheu {}\nHouve um EMPATE!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'PEDRA' and opções[escolhaJogador - 1] == 'TESOURA':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO computador ganhou!!!{}'.format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'PEDRA' and opções[escolhaJogador - 1] == 'PAPEL':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO jogador ganhou!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'PAPEL' and opções[escolhaJogador - 1] == 'TESOURA':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO jogador ganhou!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'PAPEL' and opções[escolhaJogador - 1] == 'PEDRA':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO computador ganhou!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'TESOURA' and opções[escolhaJogador - 1] == 'PAPEL':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO computador ganhou!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))

    elif opções[escolhaPc] == 'TESOURA' and opções[escolhaJogador - 1] == 'PEDRA':
        print('{}O computador escolehu {}\nO jogador escolheu {}\nO jogador ganhou!!!{}' .format(style['Azul'], opções[escolhaPc], opções[escolhaJogador - 1], style['Clear']))
    print('-=' * 15)

    jogar = int(input("""\033[36m
0 - Terminar jogo
1 - Continuar jogando\033[m
"""))

    if jogar == 1:
        print(clear)
else:
    exit()