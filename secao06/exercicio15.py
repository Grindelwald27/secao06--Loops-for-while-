num = int(input('Informe um número: '))
contador = 1
while num < 0:
    num = int(input('Informe um número: '))
while num % 2 == 0:
    num = int(input('Informe um número: '))
for contador in range(1, num + 1):
    if contador % 2 != 0:
        print(contador)
