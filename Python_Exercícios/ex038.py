from datetime import date

anoNascimento = int(input('\033[1mInforme o ano em que você nasceu:\033[m '))
gênero = int(input("""\033[1mInforme seu sexo:
1 - Masculino
2 - Feminino\033[m
"""))

idade = date.today().year - anoNascimento

if idade > 0:
    if gênero == 1:
        print('\033[34mVocê tem {} anos\033[m'.format(idade))
        if idade < 18:
            print('\033[32mVocê ainda não precisa se alistar para o serviço militar! Ainda falta(m) {} ano(s) para você poder se alistar lá em {}.\033[m'
                  .format(18 - idade, anoNascimento + 18))
        elif idade == 18:
            print('\033[33mVocê precisa se alistar para o serviço militar!')
        else:
            print('\033[31mJá passou do tempo para se alistar no serviço militar! Você deveria ter se alistado {} ano(s) atrás lá em {}!\033[m'
                  .format(idade - 18, date.today().year - (idade - 18)))
    else:
        print('\033[34mSeu alistamento não é obrigatório!!!\033[m')
else:
    print('\033[31mInforme um ano válido!!!\033[m')
