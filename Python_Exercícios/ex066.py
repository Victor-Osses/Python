from random import randint
qtdAcertos = 0

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')

while True:
    jogadaPc = randint(1, 1000)
    print('=-' * 20)
    jogadaUser = int(input('Digite um número: '))
    opçãoUser = str(input('Informe sua jogada: [PAR / ÍMPAR]: ')).lower().strip()
    soma = jogadaUser + jogadaPc

    print('-'*40)
    print(f'Você jogou {jogadaUser} e o computador {jogadaPc}! Total de {soma}')
    print('-' * 40)

    if opçãoUser == 'par':
        if soma % 2 == 0:
            print('O resultado DEU PAR. Você VENCEU!')
            print('Vamos jogar novamente...')
            qtdAcertos += 1
        else:
            print('O resultado DEU ÍMPAR. Você PERDEU!')
            print(f'GAME OVER! Você venceu {qtdAcertos} vezes')
            break
    elif opçãoUser == 'ímpar' or opçãoUser == 'impar':
        if soma % 2 != 0:
            print('O resultado DEU ÍMPAR. Você VENCEU!')
            print('Vamos jogar novamente...')
            qtdAcertos += 1
        else:
            print('O resultado DEU PAR. Você PERDEU!')
            print(f'GAME OVER! Você venceu {qtdAcertos} vezes consecutivas')
            break
