num = int(input('Informe um número: '))
soma = 0
for n in range(1, num):
    if num % n == 0:
        print(n)
        soma = soma + n
print(f'A soma é {soma}')
