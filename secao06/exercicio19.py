num = int(input('Informe um número entre 100 e 900: '))
while num < 100 or num > 900:
    num = int(input('Informe um número entre 100 e 900: '))
for algarismo in str(num):
    print(algarismo)
