print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\nPara salários '
      'superiores a R$1250,00, calcule um aumento de 10%.\nPara os inferiores ou iguais, o aumento é de 15%.')
print('')
salario = float(input('Digite o valor de seu salário atual: '))
if salario >= 1250:
    reajuste = salario + (salario * 15 / 100)
    print('Seu salario de {:.2f} sofreu um reajuste de 15%, agora você passa a receber {:.2f}'.format(salario, reajuste))
else:
   reajuste =salario + (salario * 10 / 100)
print('Seu salário de {:.2f} sofreu um reajuste de 10%, e agora você passa a receber {:.2f}'.format(salario ,reajuste))

