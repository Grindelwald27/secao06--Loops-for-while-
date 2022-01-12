contador = 1
aux = 1
soma = 0
while contador <= 50:
    if aux % 2 == 0:
        print(aux)
        contador = contador + 1
    aux = aux + 1
    soma = soma + aux
print(soma)
