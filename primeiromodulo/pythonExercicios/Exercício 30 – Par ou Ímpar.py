print('Crie um programa que leia um número inteiro\n'
      'e mostre na tela se ele é PAR ou ÍMPAR')
numero = float(input('Digite um número qualquer: '))
result = numero % 2
print('*-' * 15)
if result == 0:
    print('O resultado {:.0f} é PAR.'.format(result))
else:
    print('O resultado {:.0f} é IMPAR.'.format(result))
print('*-' * 15)

