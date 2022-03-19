print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,\n'
      'cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
distancia = float(input('Qual a distância da viajem? : '))
print('-*-' * 15)
print('A Disntência da viagem é de {:.2f}Km '.format(distancia))
if distancia <= 200:
    print('O valor da passagem para essa distância fica em R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem para essa distância fica em R${:.2f}'.format(distancia * 0.45))
print('Tenha uma boa Viajem. ')
print('-*-' * 15)
