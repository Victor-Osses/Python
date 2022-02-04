#pesquisar o módulo colorize
#print('\033[style;text;backgroundm')
#Exemplo: print('\033[0;33;40m')

print("""\n\033[7m \033[1m Códigos pra estilo que funcionam melhor no terminal python:\n
          0 - None, 1 - Bold, 4 - Underline, 7 - Negative (inverte configurações)\n
          Códigos para cor de texto:\n
          30 - Branco, 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - Roxo, 36 - ciano, 37 - cinza\n
          Códigos para background:\n
          40 - Branco, 41 - Vermelho, 42 - Verde, 43 - Amarelo, 44 - Azul, 45 - Roxo, 46 - ciano, 47 - cinza\033[m""")

print('\n\033[0;30;41m Teste 1\033[m')
print('\033[4;33;44m Teste 2\033[m')
print('\033[1;35;47m Teste 3\033[m')
print('\033[30;42m Teste 4\033[m')
print('\033[m Teste 5\033[m')
print('\033[7;30m Teste 6\033[m')

a = 3
b = 5
print('\nOs valores são \033[33m{}\033[m e \033[32m{}\033[m' .format(a, b))
nome = 'Victor'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format('\033[4;34m', nome, '\033[m'))

#Dicionário
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format(cores['amarelo'], nome, cores['limpar']))
