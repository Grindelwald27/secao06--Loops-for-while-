num = int(input('Informe um número: '))
contador = 1
aux = 1
while contador <= num:
    if aux % 2 != 0:
        print(aux)
        contador = contador + 1
    aux = aux + 1
