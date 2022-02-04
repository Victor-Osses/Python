vel = int(input('Informe a sua velocidade em Km/h: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você está acima do limite de velocidade de 80Km/h! Sua multa é de R${}', format(multa))
print('Você está dentro da velocidade limite de 80Km/h. Tenha um bom dia!')