print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias'
      ' pelos quais ele foi alugado. Calcule o preço a pagar,'
      ' sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
km = float(input('Qual foi a distância percorrida em KM?: '))
d = int(input('Por quantos dias o carro foir alugado? '))
pd = d * 60
pkm = km * 0.15
pf = pd + pkm
print('Distância Percorrida {:.2f} KM; Dias Utilizados {}: \nO valor total do aluguel ficou em '
      'R$ {:.2f}: '.format(km, d, pf))
# pago = (km * 0.15) + (d *60) Essa variável tbm funciona,
# porém tem que mudar a última impressão