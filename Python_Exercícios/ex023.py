cidade = str(input('Informe o nome da sua cidade: ')).strip()
inicio = cidade[:5].upper()
print('Forma 1: A palavra "Santo" está no início do nome da cidade:', inicio == 'SANTO')
#print('Forma 2: A palavra "Santo" está no início do nome da cidade:', 'SANTO' in cidade.split()[0].upper())
