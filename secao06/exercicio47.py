print('Escolha uma operção matemática:')
print('1 - adição')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
print('5 - saída')
opcao = int(input('Opção: '))
while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        soma = num1 + num2
        print(f'O resultado da soma é {soma}.')
        opcao = int(input('Opção: '))
    if opcao == 2:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        sub = num1 - num2
        print(f'O resultado da subtração é {sub}.')
        opcao = int(input('Opção: '))
    if opcao == 3:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        multi = num1 * num2
        print(f'O resultado da multiplicação é {multi}.')
        opcao = int(input('Opção: '))
    if opcao == 4:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        divisao = num1 / num2
        print(f'O resultado da divisão é {divisao}.')
        opcao = int(input('Opção: '))
else:
    if opcao == 5:
        print('Programa finalizado!')
