num = int(input('Informe um número inteiro: '))
maior = menor = num
while num >= 0:
    num = int(input('Informe um número inteiro: '))
    if num > maior:
        maior = num
    if num > 0:
        if num < menor:
            menor = num
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
