soma_quadrados = 0
quadrado_soma = 0
diferenca = 0
soma = 0
conta = 0
for n in range(0, 100):
    soma_quadrados = soma_quadrados + n ** 2
    quadrado_soma = soma ** 2
    diferenca = quadrado_soma - soma_quadrados
    while conta <= 100:
        soma = soma + conta
        conta = conta + 1
    n = n + 1
print(f'A soma dos quadrados de {n} é {soma_quadrados}')
print(f'Soma² = {quadrado_soma}.')
print(f'A diferença é de {diferenca}.')
