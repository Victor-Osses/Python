#Condições Aninhadas == vários "ifs" intercalados uns dentro dos outros
#elif == else + if

nome = str(input('Informe seu nome: '))
if nome == 'Victor':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!' .format(nome))
