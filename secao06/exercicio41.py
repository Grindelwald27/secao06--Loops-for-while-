r1 = int(input('Informe o valor do resistor 1: '))
r2 = int(input('Informe o valor do resistor 2: '))
while True:
    r_eq = (r1 * r2) / (r1 + r2)
    if r1 == 0 or r2 == 0:
        break
    else:
        print(f'O valor da resistência é R = {r_eq:.2f}')
        r1 = int(input('Informe o valor do resistor 1: '))
        r2 = int(input('Informe o valor do resistor 2: '))
