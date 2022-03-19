import math
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
an = float(input('Digite um ângulo: '))
se = math.sin(math.radians(an))
print('O seno de {} é {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O cosseno de {}é {:.2f}'.format(an, co))
tg = math.tan(math.radians(an))
print('a tangente de {} é {:.2f}'.format(an, tg))
