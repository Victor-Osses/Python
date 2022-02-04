from math import fabs

rt1 = float(input('Informe o comprimento do lado 1: '))
rt2 = float(input('Informe o comprimento do lado 2: '))
rt3 = float(input('Informe o comprimento do lado 3: '))

if fabs(rt2 - rt3) < rt1 < rt2 + rt3 and fabs(rt1 - rt3) < rt2 < rt1 + rt3 and fabs(rt2 - rt1) < rt3 < rt2 + rt1:
    print('As retas podem formar um triângulo!')
    if rt1 == rt2 == rt3:
        print('O triângulo formado é equilátero')
    elif rt1 != rt2 != rt3:
        print('O triângulo formado é escaleno')
    else:
        print('O triângulo formado é isósceles')
else:
    print('As retas não podem formar nenhum triângulo!!!')
