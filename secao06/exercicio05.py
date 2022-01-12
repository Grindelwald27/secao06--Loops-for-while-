print('Informe 10 números para fazermos a soma deles')
soma = 0
conta = 1
while conta <= 10:
    operando = int(input(f'Informe o {conta}º número: '))
    soma = soma + operando
    conta = conta + 1
print(f'A soma é: {soma}')
