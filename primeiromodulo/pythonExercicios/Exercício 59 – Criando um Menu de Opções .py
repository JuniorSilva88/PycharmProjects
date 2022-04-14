from time import sleep
print('CRIE UM PROGRAMA QUE LEIA 2 VALORES E MOSTRE UM MENU; O PROGRAMA TEM QUE REALIZAR AS OPERAÇÃOES SOLICITADAS')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
print('=-' * 20)
while opção != 5:
    print('''[ 1 ] - SOMAR : [ 2 ] - MULTIPLICAR : [ 3 ] - MAIOR :[ 4 ] - NOVOS VALORES: [ 5 ] - SAIR: ''')
    opção = int(input('Dentre as opções, qual você escolhe? '))
    if opção == 1:
        print('Você escolheu a opção {}: A Soma entre {} + {} = {}.'.format(opção, n1, n2, (n1 + n2)))
        print('=-' * 20)
    elif opção == 2:
        print('Você escolheu a opção {}: A Multiplicação {} x {} = {}.'.format(opção, n1, n2, (n1 * n2)))
        print('=-' * 20)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Você escolheu a opção {}: entre {} e {}, o nº {} é o Maior.'.format(opção, n1 , n2, maior))
            print('=-' * 20)
    elif opção == 4:
        print('Você escolheu a opção {}: Por favor, Digite os novos valores: '.format(opção))
        print('=-' * 20)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Finalizando...')
    sleep(1)
print('=-' * 20)
print('Fim do Programa. ')
