import random
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,'
      'lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
al1 = str(input('Qual o nome do primeiro aluno ? '))
al2 = str(input('Qual o nome do segundo aluno ? '))
al3 = str(input('Qual o nome do terceiro aluno ? '))
al4 = str(input('Qual o nome do quarto aluno ? '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno que vai apagar o quadro negro hoje será:  {} '.format(escolhido))
