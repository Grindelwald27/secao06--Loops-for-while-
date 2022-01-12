n = 20
cont = 1
while cont < 20:
    if n % cont == 0:
        cont += 1
        print(n, cont)
    else:
        n += 1
        cont = 1
print(f'O menor número divisível por todos os números de 1 a 20 é {n}')
