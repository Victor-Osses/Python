from datetime import date
anoNascimento = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - anoNascimento

if idade > 0:
    if idade > 20:
        print('Sua categoria é MASTER!!!')
    elif idade == 20:
        print('Sua categoria é SÊNIOR!!!')
    elif idade > 14 and idade <= 19:
        print('Sua categoria é JUNIOR!!!')
    elif idade > 9 and idade <= 14:
        print('Sua categoria é JUNIOR!!!')
    else:
        print('Sua categoria é MIRIM!!!')
else:
    print('Informe um ano de nascimento válido, por favor!')