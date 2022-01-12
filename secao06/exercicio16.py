num = int(input('Informe um número ímpar e positivo: '))
contador = 1
while num < 0:
    num = int(input('Informe um número ímpar e positivo: '))
while num % 2 == 0:
    num = int(input('Informe um número ímpar e positivo: '))
for contador in range(num, 0, -1):
    if contador % 2 != 0:
        print(contador)
