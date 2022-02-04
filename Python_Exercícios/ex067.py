maiorDe18 = homens = mulheresMenoresDe20 = 0
while True:
    print('-'*30 + '\n CADASTRE UMA PESSOA \n' + '-'*30)
    idade = int(input('Idade: '))
    sexo = 'a'
    continuar = '1'
    while sexo not in 'MF' or sexo == '':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if idade > 18:
        maiorDe18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenoresDe20 += 1
    while continuar not in 'SN' or continuar == '':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'\n{maiorDe18} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheresMenoresDe20} mulheres cadastradas possuem menos de 20 anos')
