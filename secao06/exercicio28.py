n = int(input('Informe um número: '))
fat = 1
i = 1
e = 1
while i <= n:
    fat = fat * i
    i = i + 1
    e = e + (1 / fat)
print(f'O valor de E é {e}')
