n = int(input('Informe o número n: '))
i = int(input('Informe o número i: '))
j = int(input('Informe o número j: '))
for a in range(0, n + 1):
    n = n + 1
    if a % i == 0:
        print(a)
    elif a % j == 0:
        print(a)
    elif a % i == 0 and a % j == 0:
        print(a)
