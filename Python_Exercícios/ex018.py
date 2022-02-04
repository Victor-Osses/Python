from random import choice
al1 = input('Informe o nome do primeiro aluno: ')
al2 = input('Informe o nome do segundo aluno: ')
al3 = input('Informe o nome do terceiro aluno(a): ')
al4 = input('Informe o nome do quarto aluno(a): ')

#lista
alunos = [al1, al2, al3, al4]

sorteado = choice(alunos)
print('\nO aluno sorteado foi o {}'.format(sorteado))