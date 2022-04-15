print('''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.''')
print('-=' * 20)
total = contador = media = maior = menor = 0
ask = 'S'
while ask == 'S':
    numeros = int(input('Digite um valor: '))
    total += numeros
    contador += 1
    if contador == 1:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    ask = str(input('Quer continuar a digitar valores ? [S/N]: ')).strip().upper()[0]
media = total / contador
print('\nE a média dos {} números digitados é {:.2f} : '.format(contador, media))
print('O maior número é {}, e o menor nº é {} : '.format(maior, menor))
print('\nFim')
print('-=' * 20)
