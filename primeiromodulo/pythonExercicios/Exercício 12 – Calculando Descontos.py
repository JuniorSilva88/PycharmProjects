print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, '
      'com 5% de desconto.')
preço = float(input('Qual o preço do item? '))
desconto = preço - (preço * 5 / 100)
print("O preço de R${:.2f}, com desconto de 5% fica: "
      "R${:.2f}.".format(preço, desconto))
