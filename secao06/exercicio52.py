nota = 0
saque = int(input('Informe o valor do saque: '))
while True:
    while saque >= 100:
        saque -= 100
        nota += 1
    while 50 <= saque < 100:
        saque -= 50
        nota += 1
    while 20 <= saque < 50:
        saque -= 20
        nota += 1
    while 10 <= saque < 20:
        saque -= 10
        nota += 1
    while 5 <= saque < 10:
        saque -= 5
        nota += 1
    while 2 <= saque < 5:
        saque -= 2
        nota += 1
    while 1 <= saque < 2:
        saque -= 1
        nota += 1
    print(f'A quantidade de notas necessárias foi: {nota}.')
    break
