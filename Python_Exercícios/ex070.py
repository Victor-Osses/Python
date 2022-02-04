números = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    continuar = ''
    valor = int(input('Digite um número entro 0 e 20: '))
    while valor <= 0 or valor >= 20:
            valor = int(input('Tente novamente. Digite um número entro 0 e 20: '))
    print(f'O número {valor} por extenso é escrito assim: {números[valor - 1]}')
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\nVocê deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
