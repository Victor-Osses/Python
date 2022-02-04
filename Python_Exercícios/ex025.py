frase = str(input('Informe uma frase qualquer: ')).strip().upper().replace(' ', '')
print('A letra "A" aparece {} vezes' .format(frase.count('A')), end='\n')
print('A primeira letra "A" está na posição {}' .format(frase.find('A') + 1))
print('A última letra "A" está na posição {}' .format(frase.rfind('A')+1))