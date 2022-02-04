nome = str(input('Informe seu nome completo: '))
print('\nSeu nome em maisculo é {}' .format(nome.upper()),
      '\nSeu nome em minusculo é {}' .format(nome.lower()),
      '\nSeu nome tem {} caracteres' .format(len(nome.replace(' ', ''))),
      '\nSeu primeiro nome tem {} caracteres' .format(len(nome.split()[0])))
