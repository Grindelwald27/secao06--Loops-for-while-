salario = 2030
ano = 1997
aumento = salario + (salario * 0.015)
while ano < 2021:
    aumento_novo = salario + (salario * 0.015 * 2)
    salario = aumento_novo
    ano += 1
    print(f'O salário atual é {salario:.2f}')
