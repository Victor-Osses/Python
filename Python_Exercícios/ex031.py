from datetime import date
ano = int(input('Informe um ano qualquer ou informe 0 para analizar o ano atual '))
if ano == 0:
    ano = date.today.year()
print('O ano de {} é bissexto!' .format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
      else 'O ano de {} não é bissexto!' .format(ano))

