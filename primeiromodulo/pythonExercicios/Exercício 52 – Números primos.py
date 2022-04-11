print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')
num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')  # se for divisivel
        tot += 1
    else:
        print('\033[31m', end=' ')  # se não for divisivel
    print('{}'.format(c), end=' ')
print('\n\033[mO Nº {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('\033[32mÉ UM Nº PRIMO!\033[m ')
else:
    print('\033[31mNÃO É UM Nº PRIMO!\033[m')
