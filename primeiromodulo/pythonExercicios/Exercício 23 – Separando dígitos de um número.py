print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'
      'Unidade / Desena / Centena / Miliar')
numero = int(input('Digite um número qualquer : '))
# num = str(numero)
und = numero // 1 % 10
dez = numero // 10 % 10
cem = numero // 100 % 10
mil = numero // 1000 % 10
print('O número digitado foi {:.0f}.'.format(numero))
print('E ele tem {} Unidades.'.format(und))
print('E ele tem {} Dezena.'.format(dez))
print('E ele tem {} Centena.'.format(cem))
print('E ele tem {} Miliar. '.format(mil))
