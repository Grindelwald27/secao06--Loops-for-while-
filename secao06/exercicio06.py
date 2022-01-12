print('Informe 10 números para fazermos a média')
soma = 0
conta = 1
while conta <= 10:
    operador = int(input(f'Informe o {conta}° número: '))
    soma = soma + operador
    conta = conta + 1
media = soma / 2
print(media)
