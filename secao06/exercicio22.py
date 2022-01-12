qtd_notas = int(input('Informe quantas notas você irá inserir: '))
total_notas = 0
media = 0
soma = 0
for n in range(1, qtd_notas + 1):
    nota = int(input(f'Informe a nota {n}/{qtd_notas}: '))
    while nota < 10 or nota > 20:
        print('Atenção! As notas devem estar entre 10 e 20.')
        nota = int(input(f'Informe a nota {n}/{qtd_notas}: '))
    if 10 <= nota <= 20:
        total_notas = total_notas + 1
        soma = soma + nota
        media = soma / qtd_notas
print(f'Você inseriu {total_notas} notas.')
print(f'Sua média é {media:.2f}')
