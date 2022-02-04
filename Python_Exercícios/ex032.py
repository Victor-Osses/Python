n1 = float(input('Informe o número 1:'))
n2 = float(input('Informe o número 2:'))
n3 = float(input('Informe o número 3:'))

maior = n1
menor = n2

if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n2 and n3 >= n1:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
if n3 <= n2 and n3 <= n1:
    menor = n3

print('O maior número é o {}' .format(maior))
print('O menor número é o {}' .format(menor))
