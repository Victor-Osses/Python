from math import hypot
catetoOpo = float(input('Informe o cateto oposto: '))
catetoAdj = float(input('Informe o cateto adjacente: '))
hipotenusa = hypot(catetoOpo, catetoAdj)
print('A medida da hipotenusa é igual a {}' .format(hipotenusa))