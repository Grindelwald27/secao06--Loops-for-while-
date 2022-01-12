print('Informe 10 números positivos para fazermos a média')
soma = 0
conta = 1
while conta <= 10:
    num = int(input(f'Informe o {conta}º número: '))
    conta = conta + 1
    while num < 0:
        num = int(input('Informe um número válido: '))
    soma = soma + num
media = soma / 2
print(media)
