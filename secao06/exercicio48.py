x = soma = 0
y = 1
while y < 4000000:
    seq = x + y
    if y % 2 == 0:
        soma += y
    x = y
    y = seq
print(f'A soma dos termos pares de Fibonacci é {soma}.')
