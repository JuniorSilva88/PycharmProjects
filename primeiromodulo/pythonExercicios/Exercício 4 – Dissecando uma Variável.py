print('Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.')
a = input('Digite algo: ')
print('O tipo primitivo digitado é', type(a))
print('Só tem espaços ?', a.isspace())
print('É um número ?', a.isnumeric())
print('É alfabético ?', a.isalpha())
print('É alphanumérico ?', a.isalnum())
print('Esta em maiúscula ?',a.isupper())
print('Esta em minúscula ?', a.islower())
print('Esta captalizada ?',a.istitle())