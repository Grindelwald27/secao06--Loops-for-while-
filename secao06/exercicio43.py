idade = int(input('Informe sua idade: '))
contador = 0
soma = 0
while idade > 0:
    soma += idade
    contador += 1
    idade = int(input('Informe sua idade: '))
    if idade == 0:
        soma += idade
        contador += idade
        print(f'A média das idades é: {soma / contador}')
        break
