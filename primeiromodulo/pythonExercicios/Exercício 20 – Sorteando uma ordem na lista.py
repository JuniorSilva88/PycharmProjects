import random
print('O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. '
      'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
al1 = str(input('Qual o nome do primeiro aluno? '))
al2 = str(input('Qual o nome do segundo aluno? '))
al3 = str(input('Qual o nome do terceiro aluno? '))
al4 = str(input('Qual o nome do quarto aluno? '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)




