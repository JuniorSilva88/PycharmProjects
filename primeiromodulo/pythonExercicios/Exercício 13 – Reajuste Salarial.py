print('Faça um algoritmo que leia o salário de um funcionário e mostre '
      'seu novo salário, com 15% de aumento.')
salário = float(input('Qual é o valor do seu salário hoje? R$ '))
reajuste = salário + (salário * 15 / 100)
print('Seu salário de é R$ {:.2f}, e tem m reajuste de 15%,\n'
      'O valor com reajuste fica em R$ {:.2f} !'.format(salário, reajuste))