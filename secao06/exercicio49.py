salario_carlos = int(input('Informe o salário de Carlos: '))
salario_joao = salario_carlos / 3
mes = 0
while salario_joao < salario_carlos:
    salario_joao += (salario_joao * 0.05)
    salario_carlos += (salario_carlos * 0.02)
    mes += 1
print(f'O salário de João demorará {mes} meses para ultrapassar o salário de Carlos.')
