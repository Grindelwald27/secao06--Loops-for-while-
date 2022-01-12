contador = 1
soma = 0
num = int(input('Informe um número: '))
while contador <= num:
    if num < 0:
        num = int(input('Informe um número positivo: '))
    else:
        soma = soma + contador
        contador = contador + 1
        print(contador - 1)
print(soma)
