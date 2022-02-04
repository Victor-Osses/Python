preçoProduto = float(input('Informe o preço do produto a ser pago: '))
formaPagamento = int(input('''
Escolha sua forma de pagamento
1 - À vista com 10% de desconto
2 - À vista no cartão com 5% de desconto
3 - Em até 2x no cartão com preço normal
4 - 3x ou mais no cartão com 20% de juros\n'''))

if formaPagamento == 1:
    preçoProduto *= 0.9
elif formaPagamento == 2:
    preçoProduto *= 0.95
elif formaPagamento == 3:
    preçoProduto = preçoProduto
    print('Sua parcela ficará em 2x de R${}' .format(preçoProduto / 2))
elif formaPagamento == 4:
    preçoProduto *= 1.2
    print('Sua parcela ficará em 3x de R${} com juros' .format(preçoProduto / 3))
else:
    print('Opção inválida de pagamento!')
    exit()
print('O preço total do produto ficará em R${:.2f}'.format(preçoProduto))
