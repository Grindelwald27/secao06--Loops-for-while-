n = int(input('Informe um valor para n: '))
hn = 0
for i in range(1, (n + 1)):
    hn = hn + (1 / i)
print(f'H {n} vale {hn}')
