print('Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, '
      'em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')
frase = str(input('Digite uma frase: ')).strip().upper()
print('Essa frase possui quantas letras "A"? R = {}'.format('A' in (frase.upper())))
print('Quantas vezes aparece essa letra? R = {}'.format(frase.count('A')))
print('Qual a primeira vez que apareceu? R = {}'.format(frase.find('A')+1))
print('Qual a última vez que apareceu? R = {}'.format(frase.rfind('A')+1))
