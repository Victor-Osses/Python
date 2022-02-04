frase = str(input('Informe uma frase qualquer: ')).replace(' ', '')
fraseInvertida = ''

for count in range(len(frase) - 1, -1, -1):
    fraseInvertida += frase[count]

if frase == fraseInvertida:
    print('A frase é um palíndromo!!!')
else:
    print('A frase não é um palíndromo!!!')
