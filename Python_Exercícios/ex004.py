algo = input('\033[1mInforme um valor qualquer: ')

coresTexto = {
    'limpar': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
    }

coresFundo = {
    'preto': '\033[40m',
    }

print('\n{}O tipo primitivo é {}{}' .format(coresTexto['preto'], type(algo), coresTexto['limpar']))
print('{}Só possuí caracteres alfabéticos: {}{}' .format(coresTexto['vermelho'], algo.isalpha(), coresTexto['limpar']))
print('{}Pode ser convertido para um número: {}{}' .format(coresTexto['verde'], algo.isnumeric(), coresTexto['limpar']))
print('É alfanúmerico: {}'.format(algo.isalnum()))
print('A string é ASCII: {}' .format(algo.isascii()))
print('Todos os caracteres são digitos (números): {}' .format(algo.isdigit()))
print('É um decimal: {}' .format(algo.isdecimal()))
print('Todos os caracteres são válidos para escrever um identificador no código: {}' .format(algo.isidentifier()))
print('Todos os caracteres estão em letra minuscula: {}' .format(algo.islower()))
print('Pode ser printado: {}' .format(algo.isprintable()))
print('É um espaço: {}' .format(algo.isspace()))
print('Todas as palavras começam com letra maiuscula: {}' .format(algo.istitle()))
print('Está tudo em letra maiscula: {}' .format(algo.isupper()))
