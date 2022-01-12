a = int(input('Informe um número inicial maior que 1: '))
b = int(input('Informe um número final: '))
conta = 0
while a > b or a < 2:
    a = int(input('Informe um número inicial maior que 1: '))
for n in range(a, b + 1):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        conta += 1
print(f'A quantidade de números primos ente {a} e {b} é {conta}.')
