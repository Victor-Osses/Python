#Soma: +, Subtração: -, Multiplicação: *, Divisão: /, Potência: **, Divisão Inteira: //, Resto da Divisão: %

print('\nSoma:', 1+2)
print('Subtração:', 1-2)
print('Multiplicação:', 1*2)
print('Divisão:', 1/2)
print('Potência:', 1**2)
print('Divisão Inteira', 1//2)
print('Resto de divisão:', 2 % 2 == 0)

print('\nOrdem de precedência:\n'
      '1 - ()\n'
      '2 - **\n'
      '3 - *,/,//,%\n'
      '4 - +,-')

#testes
print('\n', '=' * 10, 'TESTES', '=' * 10, '\n')

print(5+5)
print(10-22)
print(20*3)
print(25/4)
print(22//12)
print(222**22)
print(81**(1/2))
print(pow(2, 2))
print(124 % 3)

nome = str(input('\nQual é seu nome? '))

print('Prazer em te conhecer, {:20}!' .format(nome))
print('Prazer em te conhecer, {:>20}!' .format(nome))
print('Prazer em te conhecer, {:<20}!' .format(nome))
print('Prazer em te conhecer, {:^20}!' .format(nome))
print('Prazer em te conhecer, {:=^20}!' .format(nome))

n1 = int(input('\nUm valor: '))
n2 = int(input('Outro valor: '))
print('\n')
s = n1+n2
m = n1*n2
d= n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}, o produto vale {} e a divisão é {:.3f}' .format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}' .format(di, e))

print('\n', '=' * 10, 'FIM DOS TESTES', '=' * 10, '\n')


