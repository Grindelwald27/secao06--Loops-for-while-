num = int(input('Informe um número: '))
soma1 = soma2 = soma3 = 0
s2 = 1 - 2 + 3 - 4 + 5
for n in range(1, num + 1):
    soma1 = soma1 + n
print(f'O resultado da primeira equação é {soma1}')
for n in range(1, 2 * num):
    soma2 = soma2 + s2 + n
print(f'O resultado da segunda equação é {soma2}')
for n in range(1, 2 * num, 2):
    soma3 = soma3 + n
print(f'O resultado da terceira equação é {soma3}')
