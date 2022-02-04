frase = 'Curso em vídeo de Python'
#frase[0] = 'j' Não funciona, pois uma string é imutável, só com o método replace eu consigo mudar

#Fatiamento
print(frase[9])
print(frase[9:15])#pega do caractér 9 até o 14
print(frase[9:22:2])#do 9 até o 20 pulando de 2 em 2 caractéres
print(frase[:5])#Começa do caractére 0 e vai até a letra 4
print(frase[15:])#Começa do 15 e vai até o final
print(frase[9::3])#Começa no 9 e vai até o final pulando de 3 em 3 caractéres
                
#Consultas
print(len(frase), 'caracteres')
print('Existem', frase.count('o', 0, 13), 'letras o da posição até a 12')
print(frase.find('deo'))#Indica em que posição começa essa sequência
print(frase.find('Android'))#-1 significa que não foi encontrado
print('Curso' in frase)#Existe a palavra 'Curso' em frase? True!

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.title())#Todas as letras do inicio de cada palavra começam com letra maiscula
print(frase.capitalize())#Só o primeiro caractere fica em maiusculo
print(frase.strip())#remove todos os espaços no inicio e no fim da string
print(frase.rstrip())#remove todos os espaços no fim (a direita) da string
print(frase.lstrip())#remove todos os espaços no inicio (a esquerda) da string
print(frase.split())#cria uma lista com as palavras da string inicial
dividido = frase.split()
print("Pegando a letra de uma palavra de uma lista:", dividido[2][3])
print('-'.join(frase))

print("""Da pra escrever um texto grande assim
viuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu""")