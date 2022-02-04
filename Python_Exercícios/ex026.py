nome = str(input('Informe seu nome completo: ')).strip()
nomeDiv = nome.split()
print('Primeiro nome: {}\nÚltimo nome: {}' .format(nomeDiv[0], nomeDiv[len(nomeDiv) - 1]))
