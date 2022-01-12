print('Informe 10 números')
maior = menor = 0
for n in range(1, 11):
    num = int(input(f'Informe o {n}° número: '))
    if n == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
