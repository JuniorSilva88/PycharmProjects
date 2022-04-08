print('''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros''')
preço = float(input('Qual valor do produto: R$ '))
print('''[1]- A vista Dinheiro ou Cheque:
[2]- A vista Débito:
[3]- 2x no C.Crédito:
[4]- 3x ou mais no C.Crédito:''')
opção = int(input('Qual será a forma de pagamento: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parctotal = int(input('Em quantas vezes quer parcelar sua compra? '))
    parcela = total / parctotal
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(parctotal, parcela))
else:
    total = 0
    print('Opção inválida')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final. '.format(preço, total))



