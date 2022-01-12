n = 0
par = 0
soma = 0
while n != 1000:
    num = int(input('Informe um número: '))
    n = num
    if num != 1000:
        soma = soma + 1
    if num % 2 == 0 and num != 1000:
        print(f'O número {num} é par')
        par = par + 1
print(f'Número de dados lidos: {soma}')
print(f'Números pares lidos: {par}')
