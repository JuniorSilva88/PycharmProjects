print('''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– \033[32;1mO primeiro valor é maior\033[m
– \033[34;1mO segundo valor é maior\033[m
– \033[31;1mNão existe valor maior, os dois são iguais\033[m''')
num1 = int(input(' Digitte um número inteiro : '))
num2 = int(input(' Digite outro número inteiro : '))
print(' Os 2 números digitados são : \033[32;4mnº {}\033[m, \033[34;4mnº {}\033[m'.format(num1, num2))
if num1 > num2:
    print(' \033[32;4mO primeiro valor é maior\033[m')
elif num2 > num1:
    print(' \033[34;4mO segundo valor é maior!\033[m ')
else:
    print(' \033[31;1mNão existe valor maior, os 2 sãos iguais!\033[m ')
