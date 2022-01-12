print('Descubra se determinado número é positivo!')
num = int(input('Informe um número inteiro maior que 1: '))
for n in range(2, num - 1):
    if num % n == 0:
        print(f'{num} não é um número primo.')
    if num % n != 0:
        print(f'{num} é um número primo.')
    break
