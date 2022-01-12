print('Informe 2 números (a, b) e receba um terceiro número (c) cuja soma dos três será igual a 1000.')
a = int(input('Informe o número a: '))
b = int(input('Informe o número b: '))
c = a ** 2 + b ** 2
while a + b + c != 1000:
    print('Erro! A soma dos números deve ser igual a 1000.')
    a = int(input('Informe o número a: '))
    b = int(input('Informe o número b: '))
    if c == a ** 2 + b ** 2 == 1000:
        print(f'O valor de c² é: {c} ')
