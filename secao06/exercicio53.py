n = int(input('Informe um número que seja inteiro e positivo: '))
soma = 0
for i in range(1, n + 1):
    soma += i
    for num in range(soma - i + 1, soma + 1):
        print(num, end=' ')
    print()
