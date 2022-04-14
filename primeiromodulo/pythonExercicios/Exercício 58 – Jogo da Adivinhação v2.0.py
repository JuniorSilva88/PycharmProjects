from random import randint
from time import sleep
print('''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.''')
print('*-' * 20)
pc = randint(0, 10)
print('Vou escolher entre 0 e 10: Quantas jogadas você precisa para adivinhar? ')
print(' 🤔 🤔 🤔')
acertou = False
palpite = 0
sleep(1.25)
while not acertou:
    jogador = int(input('Bora lá. Qual número eu escolhi? '))
    palpite += 1
    if pc == jogador:
        acertou = True
    else:
        if jogador < pc:
            print('Errou 🤣 🤣 🤣 Escolhi um nº MAIOR...\nVamos 🦆 tente mais uma vez.')
        elif jogador > pc:
            print('Errou 🤣 🤣 🤣 Escolhi um nº MENOR...\nVamos 🦆 tente mais uma vez.')
print('\033[32m🎆 🎆 🎆 🎆 🎆 🎆 🎆 🎆 🎆 \033[m')
print('Acertou com {} jogadas'.format(palpite))
