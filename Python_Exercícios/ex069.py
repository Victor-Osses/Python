sacar = int(input('Informe quanto de dinheiro você deseja sacar: R$'))
total = sacar
cédAtual = 50
qtdCéd = 0
while True:
    if total >= cédAtual:
        total -= cédAtual
        qtdCéd += 1
    else:
        print(f'Você sacou {qtdCéd} cédulas de R${cédAtual}')
        if cédAtual == 50:
            cédAtual = 20
        elif cédAtual == 20:
            cédAtual = 10
        elif cédAtual == 10:
            cédAtual = 1
        if cédAtual == 1:
            break
        qtdCéd = 0
