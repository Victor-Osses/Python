qtdKmPercorridos = float(input('\nInforme quantos quilômetros foram percorridos com o veículo: '))
qtdDiasAlugados = float(input('Informe por quantos dias o veículo foi alugado: '))
print('\nO preço a ser pago é R${:.2f}' .format(qtdKmPercorridos*0.15 + qtdDiasAlugados*60))