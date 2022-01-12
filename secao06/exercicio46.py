import random
num = random.randint(1, 1000)
contador = 0
chute = int(input('Adivinhe o número escolhido pelo programa: '))
while chute != num:
    if chute < num:
        print(f'Errou! O número é maior que {chute}.')
        chute = int(input('Adivinhe o número escolhido pelo programa: '))
        contador += 1
    if chute > num:
        print(f'Errou! O número é menor que {chute}.')
        chute = int(input('Adivinhe o número escolhido pelo programa: '))
        contador += 1
if chute == num:
    contador += 1
    print(f'Você acertou! O número {num} é igual a {chute}.')
    print(f'Você fez {contador} tentativas.')
