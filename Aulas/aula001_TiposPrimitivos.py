#tipos primitivos: int, float, bool (True or False) e str
#Aspas simples são recomendadas por uma questão estética

n1 = input('Digite um número: ')
typeN1 = type(n1)
n1 = int(n1)
n2 = int(input('Digite mais um número: '))

print("\nTipo de n1 quando armazenado:", typeN1)
print("Tipo de n1 quando feito o casting:", type(n1))
print("Forma 1 de concatenar:", n1 + n2)
print("Forma 2 de concatenar: {}" .format(n1 + n2))
print("A soma entre {1} e {0} vale {2}" .format(n1, n2, n1+n2))

n3 = float(input('\nInforme um valor inteiro: '))
print('\nValor: {}\nTipo: {}' .format(type(n3), n3))

boolean = bool(input('\nDigite um valor (ou não) e veja o que o boolean retorna: '))
print("\n{}" .format(boolean))

#métodos de teste de tipo
n4 = input('\nDigite algo: ')
print('\nFunção isnumeric() retornará true se o parâmetro informado pode ser convertido para um número: {}' .format(n4.isnumeric()))
print('\nFunção isalpha() retornará true se o parâmetro informado é alfabético (só tem letras): {}' .format(n4.isalpha()))
print('\nFunção isalnum() retornará true se o parâmetro informado é alfa-numérico: {}' .format(n4.isalnum()))

