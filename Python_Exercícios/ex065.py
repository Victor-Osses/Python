while True:
    tabuada = int(input('Informe um número inteiro (Digite um valor negativo para sair): '))
    if tabuada < 0:
        break
    print(f'\nTABUADA DO {tabuada}:')
    for count in range(1, 11):
        print(f'{count} x {tabuada} = {count * tabuada}')
    print('\n')
