num = int(input('Informe um número: '))
for n in range(1, num+1):
    if num % n == 0:
        print(n)
