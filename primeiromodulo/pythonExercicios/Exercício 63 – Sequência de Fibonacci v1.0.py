print('ESCREVA UM PROGRAMA QUE LEIRA UM Nº INTEIRO QUALQUER E MOSTRE NA TELA OS Nº PRIMEIROS ELEMENTOS DE UMA SEQUENCIA'
      'DE FIBONACCI. EXEMPLO  0➡ 1➡ 1➡ 2➡ 3➡ 5➡ 8')
print('¬=' * 15)
print('\033[43;1mSEQUENCIA DE FIBONACCI\033[m  ')
print('¬=' * 15)
numero = int(input('Digite um número que represete a quantidade de termos que queira calcular: '))
termo1 = 0
termo2 = 1
print('¬=' * 15)
print('{} ➡ {}'.format(termo1, termo2), end='')
contador = 3
while contador <= numero:
     termo3 = termo1 + termo2
     print(' ➡ {}'.format(termo3), end='')
     contador += 1
     termo1 = termo2
     termo2 = termo3
print(' \nFim')
print('¬=' * 15)
