import random
qtd = int(input('Informe a quantidade de vezes que os dados devem rodas: '))
for n in range(1, qtd + 1):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        print(f'O resultado do dado 1 é {dado1}')
        print(f'O resultado do dado 2 é {dado2}')
        print(f'O dado 1 é igual ao dado 2 : {dado1} = {dado2}')
    elif dado1 > dado2:
        print(f'O resultado do dado 1 é {dado1}')
        print(f'O resultado do dado 2 é {dado2}')
        print(f'O dado 1 é maior que o dado 2 : {dado1} > {dado2}')
    elif dado1 < dado2:
        print(f'O resultado do dado 1 é {dado1}')
        print(f'O resultado do dado 2 é {dado2}')
        print(f'O dado 1 é menor que o dado 2 : {dado1} < {dado2}')
