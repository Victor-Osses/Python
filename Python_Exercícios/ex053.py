from datetime import date
maiores = 0
menores = 0
anoAtual = date.today().year

for count in range(1, 8):
    anoNascimento = int(input('Informe o ano em que nasceu: '))
    if anoNascimento <= anoAtual:
        idade = anoAtual - anoNascimento
        if idade >= 21:
            maiores += 1
        else:
            menores += 1

print('\nO número de pessoas maiores de idade é {}' .format(maiores))
print('O número de pessoas menores de idade é {}' .format(menores))
