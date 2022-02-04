preçoTotal = qtdPreçoMaiorQue100 = preçoProdMaisBarato = 0
nomeProdMaisBarato = ''
while True:
    print('-'*30)
    print('CADASTRE UM PRODUTO')
    print('-' * 30)
    nomeProd = str(input('Nome do produto: '))
    preçoProd = float(input('Preço do produto: R$'))
    if preçoTotal == 0:
        preçoProdMaisBarato = preçoProd
        nomeProdMaisBarato = nomeProd
    elif preçoProd < preçoProdMaisBarato:
        preçoProdMaisBarato = preçoProd
    if preçoProd > 1000:
        qtdPreçoMaiorQue100 += 1
    preçoTotal += preçoProd
    continuar = ''
    while continuar not in 'SN' or continuar == '':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print('-'*20, 'FIM DO PROGRAMA', '-'*20)
print(f'O total gasto na compra foi de R${preçoTotal:.2f}')
print(f'O total de produtos que custam mais de R$1000.00 foi de {qtdPreçoMaiorQue100} produtos')
print(f'O produto mais barato se chama {nomeProdMaisBarato} e custa R${preçoProdMaisBarato:.2f}')
