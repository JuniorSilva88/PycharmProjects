from math import factorial
print('\033[40;1;7mFAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE SEU FATORIAL, '
      'EXEMPLO: 5! = 5 X 4 X 3 X 2 X 1 = 120\033[m')
print('\033[32;1m-=\033[m' * 20)
num = int(input('Digite um número: '))
fac = factorial(num)
print('O nº digitado foi {}. E seu FATORIAL é {}! = {}'.format(num, num, fac))  # metodo utilizando biblioteca
print('\033[36;1m¬*\033[m' * 20)
print('')
num = int(input('Digite um Número : '))
calc = num
fac = 1
print('Calculando \033[35;1m{}!\033[m = '.format(num), end='')
while calc > 0:
    print('{}'.format(calc), end='')
    print(' x ' if calc > 1 else ' = ', end='')
    fac *= calc
    calc -= 1
print('\033[35;1m{}!\033[m'.format(fac))  # metodo utilizando while
print('\033[36;1m¬*\033[m' * 20)

