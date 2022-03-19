import math
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. '
      'Calcule e mostre o comprimento da hipotenusa.')
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Catato Adjascente: '))

'''hip = (co ** 2 + ca ** 2) ** (1/2)
print('{} . {} = {:.2f} '.format(co, ca, hip))'''

hip = math.hypot(co, ca)
print('{}  e {} = {:.2f}'.format(co, ca, hip))
