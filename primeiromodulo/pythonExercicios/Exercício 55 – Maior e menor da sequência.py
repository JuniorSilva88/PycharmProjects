print('''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.''')
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:  # maior peso
            maior = peso  # passa a ser o maior
        if peso < menor:  # menor peso
            menor = peso  # passa a ser o menor
print('O maior peso lido foi de {}Kg '.format(maior))
print('O menor peso lido foi de {}Kg. '.format(menor))
