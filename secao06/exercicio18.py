cont_max = 0
num_max = -1
quant = int(input('Informe quantos números se quer utilizar: '))
for n in range(0, quant, 1):
    num = int(input(f'Informe os números: {n + 1}/{quant}: '))
    if num > num_max:
        num_max = num
        cont_max_ = 0
        cont_max = 1
    elif num_max == num:
        cont_max += 1
print(f'O maior número é: {num_max}. Este apareceu {cont_max} vezes')
