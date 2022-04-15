from time import sleep
print('''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados 
e qual foi a soma entre eles (desconsiderando o flag).''')
print('\033[32;1m+=\033[m' * 35)
numero = 0
contador = 0
total = 0
while numero != 999:  # enquanto numero for diferente de 999, solicitar para digitar novamente
    numero = int(input('Digite um novo valor ou digite o \033[34;1mNº 999\033[m para Pausar o programa: '))   # digite o nº escolhido
    total += numero  # soma total de nº digitados
    contador += 1  # contador recebe mais um
print('\nForam digitados {} números, e a soma total dos números é = {}. '.format((contador-1), (total - 999)))
print('\nFinalizando programa. ')
sleep(.50)
print('. ', end='')
sleep(.50)
print('. ', end='')
sleep(.50)
print('. ', end='')
sleep(.50)
print(' Fim')
print('\033[32;1m+=\033[m' * 35)
