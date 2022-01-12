num = int(input('Informe um número: '))
contador = 1
par = 1
while num % 2 != 0:
    num = int(input('Informe um número: '))
for contador in range(0, num + 1):
    if par % 2 == 0:
        print(par)
    par = par + 1
contador = contador + 1
