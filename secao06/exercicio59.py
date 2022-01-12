num_hab = 5
hab = 0
n_cod = 0
maior = 0
menor = 0
while hab < num_hab:
    cons_mes = int(input('Informe seu consumo: '))
    print('Código do consumidor: \n'
            '1 - Residencial \n' 
            '2 - Comercial \n'
            '3 - Industrial')
    codigo = int(input('Informe seu código: '))
    if codigo == 1:
        print('Residencial')
        n_cod += 1
    if codigo == 2:
        print('Comercial')
        n_cod += 1
    if codigo == 3:
        print('Industrial')
        n_cod += 1
    hab += 1
    n_cod += 1
