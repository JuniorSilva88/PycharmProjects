print('''Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas
estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper 
um laço no meio do caminho.
Além disso, vamos aprender como trabalhar com as novas fstrings do Python.''')
cont = 1
while cont <= 10:  # tem uma condição de parada
    print(cont, end=' ')
    cont += 1
print(' Fim')
print('')
# while True:  # enquanto for verdadeiro, comtinua, porém não tem condição de parada
#    print(cont, end=' ')
#    cont += 1
#  print(' Fim')
# print('')
n = 0
while True:  # equanto for verdadeiro , continuar
    print(cont, end=' ')
    n = int(input('Digite um número: '))
    if n == 999:
        break  # porém se o número for 999 condição de parada , para e sai do laço utilinazo o break
    cont += 1
print(' Fim')

print('')
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
soma = n1 + n2
print(f'A soma de {n1, n2} é {soma}')  # utilizando fstrings atualização do python apartir 3.6
