from math import sin, cos, tan, radians
seno = float(input('Informe o seno do ângulo: '))
cosseno = float(input('Informe o cosseno do ângulo: '))
tangente = float(input('Informe a tangente do ângulo: '))
print('\nO seno de {:.2f} é igual a {:.2f}\n'
      'O cosseno de {:.2f} é igual a {:.2f}\n'
      'A tangente de {:.2f} é igual a {:.2f}'
      .format(seno, sin(radians(seno)), cosseno, cos(radians(cosseno)), tangente, tan(radians(tangente))))