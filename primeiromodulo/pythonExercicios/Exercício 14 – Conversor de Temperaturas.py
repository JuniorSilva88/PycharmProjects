print('Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
C = float(input('Qual a temperatura atual ºC ? '))
F = C * 9 / 5 + 32
K = C + 273.15
print(' {:.2f}ºC é o equivalente a {:.2f} ºF;\n E {:.2f} ºC '
      'é o equivalente há {:.2f} ºK.'.format(C, F, C, K))