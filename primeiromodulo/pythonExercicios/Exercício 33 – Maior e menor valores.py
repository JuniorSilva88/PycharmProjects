print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# verificando menor
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
# verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > b and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
