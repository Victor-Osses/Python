n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua primeira nota: '))
média = (n1 + n2) / 2

if média > 0:
    if média >= 7:
        print('\033[32mSua média foi {} e você está aprovado!!!\033[m' .format(média))
    elif 5 <= média <= 6.9:
        print('\033[33mSua média foi {} e você está de recuperação!!!\033[m' .format(média))
    else:
        print('\033[31mSua média foi {} e você está reprovado!!!\033[m'.format(média))