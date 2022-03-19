print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um '
      'triângulo.')
print('~'*50)
a = float(input('Digite o valor de Seguimento A: '))
b = float(input('Digite o valor de Seguimento B: '))
c = float(input('Digite o valor de Seguimento C: '))
if a < b + c and b < a + c and c < b + a:
      print('a soma dos seguimentos A, B e C PODEM formar um Triângulo. ')
else:
      print('A soma dos seguimentos A, B e C NÃO PODEM formar um Triângulo. ')
