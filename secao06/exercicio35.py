n_inicio = int(input('Informe um número de inicial: '))
n_final = int(input('Informe um número final: '))
soma = 0
impar = 1
if n_inicio > n_final:
    print('Intervalo de valores inválido. O número inicial deve ser menor que o final.')
    n_inicio = int(input('Informe um número de inicial: '))
    n_final = int(input('Informe um número final: '))
else:
    for n in range(n_inicio, n_final):
        if n % 2 != 0:
            soma = soma + n
            print(n)
print(f'A soma dos ímpares neste intervalo é {soma}.')
