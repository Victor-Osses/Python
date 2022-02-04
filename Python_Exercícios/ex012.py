preco = float(input('Informe o preço do produto que terá desconto de 5%: '))
salario = float(input('Informe o salário que será aumentado em 15%: '))

print('Novo preço do produto: R${:.2f}\nNovo salário: R${:.2f}' .format(0.95*preco, salario*1.15))