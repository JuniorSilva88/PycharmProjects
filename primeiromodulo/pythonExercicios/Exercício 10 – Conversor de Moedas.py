print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
moeda = float(input('Qual valor você tem ai na carteira? R$ '))
dolar = moeda / 5.33
libras = moeda / 7.21
iene = moeda / 0.066
euro = moeda / 6.10
print('Com essa quantidade em R$ {:.2f}, você tem o equivalente há: \n'
      'Esse valor em Dólares U${:.2f};\n'
      'Esse valor em Libras £ {:.2f};\n'
      'Esse valor em Iene ¥ {:.2f};\n'
      'Esse valor em Euro € {:.2f}\n'
      'Nas respectivas cotaçãoes atuais.'.format(moeda, dolar, libras, iene, euro))