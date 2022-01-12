altura = float(input('Informe o valor da altura do triângulo: '))
base = float(input('Informe o valor da base do triângulo: '))
while True:
    while altura <= 0:
        print('Erro! O valor da altura deve ser maior que 0')
        altura = float(input('Informe o valor da altura do triângulo: '))
    while base <= 0:
        print('Erro! O valor da base deve ser maior que 0')
        base = float(input('Informe o valor da base do triângulo: '))
    area = (base * altura) / 2
    print(f'A área do triângulo é {area}cm² ')
    break
