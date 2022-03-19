from random import randint
from time import sleep
print('Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário\n'
      'tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário\n'
      'venceu ou perdeu.')
num = randint(0, 5)
escolha = float(input('Qual número acha que foi escolhido? '))
print('-*-' * 10)
print('Processando...')
sleep(3)
if escolha == num:
    print('Legal você acertou.\nRealmente escolhemos o número : {}'.format(num))
else:
    print('Qua pena você errou.\nPorque esolhemos o número : {}'.format(num))
print('-*-' * 10)
