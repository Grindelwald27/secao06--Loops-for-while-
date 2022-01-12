num = int(input('Informe um número: '))
while num % 11 != 0:
    num = num + 1
    if num % 11 == 0:
        print(f'O primeiro múltiplo de 11 é {num}')
while num % 13 != 0:
    num += 1
    if num % 13 == 0:
        print(f'O primeiro múltiplo de 13 é {num}')
while num % 17 != 0:
    num += 1
    if num % 17 == 0:
        print(f'O primeiro múltiplo de 17 é {num}')
