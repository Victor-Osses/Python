from math import fabs
rt1 = float(input('Informe o comprimento da primeira reta: '))
rt2 = float(input('Informe o comprimento da primeira reta: '))
rt3 = float(input('Informe o comprimento da primeira reta: '))

#fabs retorna o valor absoluto de um número
if fabs(rt2 - rt3) < rt1 < rt2 + rt3 and fabs(rt1 - rt3) < rt2 < rt1 + rt3 and fabs(rt2 - rt1) < rt3 < rt2 + rt1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo')