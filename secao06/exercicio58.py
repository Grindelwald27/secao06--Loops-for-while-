a = int(input('Informe um número inicial maior que 1: '))
b = int(input('Informe um número final maior que o número inicial: '))
soma = 0
for n in range(a, b + 1):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        soma += n
print(soma)
