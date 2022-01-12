print('Escolha uma das opções abaixo: ')
print('1 - Transformar uma velocidade de km/h para m/s')
print('2 - Transformar uma velocidade de m/s para km/h')
print('3 - Finalizar o programa')
opcao = int(input('Opção: '))
while opcao == 1 or opcao == 2:
    if opcao == 1:
        velocidade = int(input('Informe a velocidade: '))
        conversao = velocidade / 3.6
        print(f'A velocidade é {conversao} m/s.')
    opcao = int(input('Opção: '))
    if opcao == 2:
        velocidade = int(input('Informe a velocidade: '))
        conversao = velocidade * 3.6
        print(f'A velocidade é {conversao} km/h')
    opcao = int(input('Opção: '))
else:
    if opcao == 3:
        print('Programa encerrado!')
