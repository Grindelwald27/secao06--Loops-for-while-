soma = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        soma = soma + n
print(f'A soma dos múltiplos de 3 e 5 é {soma}')
