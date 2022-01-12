num = int(input('Informe um número: '))
ultimo = 1
penultimo = 1
for n in range(0, num):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo > num:
        print(termo)
        break
    else:
        print(termo)
