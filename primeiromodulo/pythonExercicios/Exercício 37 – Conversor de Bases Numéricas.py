print('Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a\n '
      'base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.')
n1 = int(input('Digite um numero: '))
print('''Escolha uma base numérica parac conversão:
Sendo:
[1] Converter para BINÁRIO;
[2] Converter para OCTAL;
[3] Converter para HEXADECIMAL;''')
escolha = int(input('Qual sua opção? '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual há {} .'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual há {} .'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual há {} .'.format(n1, hex(n1)[2:]))
else:
    print('Você digitou um número não válido!')
