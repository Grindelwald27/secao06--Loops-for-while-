num = int(input('Informe um número inteiro não negativo: '))
ciclo = 0
soma = 0
numero = 2
while ciclo < num:
    divisores = 0
    for n in range(1, numero + 1):
        if numero % n == 0:
            divisores += 1
    if divisores == 2:
        soma += numero
        ciclo += 1
    numero += 1
print(f'A soma dos {num} primeiros números primos é {soma}.')
