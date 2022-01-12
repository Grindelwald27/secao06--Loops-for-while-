num = int(input('Informe um número par e positivo: '))
contador = 1
while num < 0:
    num = int(input('Informe um número par e positivo: '))
while num % 2 != 0:
    num = int(input('Informe um número par e positivo: '))
for conta in range(num, -1, -1):
    if conta % 2 == 0:
        print(conta)
