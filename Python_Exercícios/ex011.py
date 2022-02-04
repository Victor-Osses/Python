largura = float(input('\nInforme a largua da sua parade' ))
altura = float(input('Informe a altura da sua parede '))
area = largura * altura
qtdTinta = area / 2
print('\nA área da sua parede é de {:.2f}m² e você precisará de {:.2f} litros para pinta-lá' .format(area, qtdTinta))