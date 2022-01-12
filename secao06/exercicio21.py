par = 0
impar = 1
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
for n in range(num1, num2 + 1):
    if n % 2 == 0:
        par = par + n
    if n % 2 != 0:
        impar = impar * n
print(par)
print(impar)
