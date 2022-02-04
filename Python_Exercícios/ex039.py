peso = float(input('Informe sua massa corporal: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura**2)

if imc > 40:
    print('Seu IMC é {:.2f} e seu status é obesidade mórbida' .format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f} e seu status é obesidade' .format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f} e seu status é sobrepeso' .format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f} e seu status é peso ideal' .format(imc))
else:
    print('Seu IMC é {:.2f} e seu status é abaixo do peso' .format(imc))