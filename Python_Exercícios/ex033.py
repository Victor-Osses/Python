salario = float(input('Informe o seu sálario atual: '))
print('Seu novo sálario será de  R${:.2f}' .format(salario*1.10)
      if salario > 1250 else 'Seu novo sálario será de R${:.2f}' .format(salario*1.15))
