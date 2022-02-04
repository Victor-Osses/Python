valorCasa = float(input('Informe o valor da casa: '))
salário = float(input('Informe seu sálario: '))
tempo = int(input('Informe em quantos anos você pretende pagar: '))
prestaçãoMensal = valorCasa / (tempo * 12)

print('\033[33m\nO valor da prestação mensal é de {:.2f} e seu sálario é de {:.2f}.\033[m' .format(prestaçãoMensal, salário))
if(prestaçãoMensal <= salário * 0.3):
    print('\033[32mDito isso, seu empréstimo foi concedido!\033[m')
else:
    print('\033[31mDito isso, seu empréstimo foi negado!\033[m')