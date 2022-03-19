print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo\n'
      'que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')
speed = float(input('Qual a velocidade do carro? '))
print('-*-' * 10)
if speed > 80:
    print('Você excedeu o limete de velocidade 80Km/h.')
    multa = (speed - 80) * 7
    print('Por isso tem uma multa a ser paga de: R$ {:.2f}'.format(multa))
else:
    print('Continue se dirigindo em segurança. ')
print('-*-' * 10)
