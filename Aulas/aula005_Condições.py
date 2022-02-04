idadeCarro = int(input('Informe a quanto tempo você tem seu carro: '))
print('\n')

#O python trabalha com identação: tudo que estiver dentro de uma condição deve ter identação adequada
if idadeCarro <= 3:
    print('O seu carro ainda tá novinho!')
else:
    print('O seu carro já tá meio velho...')

#Não existe operador ternário em python, mas esse jeito é parecido
print('carro novo' if idadeCarro <=3 else '\ncarro velho')