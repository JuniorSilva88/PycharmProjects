from random import randint
from time import sleep
print('''FAÇA UM PROGRAMA QUE JOGE PAR OU IMPAR CONTRA O COMPUTADOR. O JOGO SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER.
MOSTRE O TOTAL DE VITÓRIAS CONSCUTIVAS QUE ELE CONSQUISTOU NO FINAL DO JOGO!''')
print('^' * 40)
print('====\ JOGO DO PAR OU IMPAR /==== ')
win = 0
while True:
    gamer = int(input('Um valor: '))
    computador = randint(0, 10)
    total = gamer + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [P/I] ? ')).strip().upper()
    print(f'Você jogou {gamer} e o computador {computador} .Total de {total}', end='  ')
    sleep(2)
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('YOU WIN!!! ')
            win += 1
        else:
            print('YOU OVER!!!  🦆 🦆 🦆')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('YOU WIN!!! ')
            win += 1
        else:
            print('YOU OVER!!!  🦆 🦆 🦆')
            break
    sleep(1)
    print('Vamos jogar novamente... ')
print(f'GAMER OVER 🤣 🤣 🤣 ...   Você venceu {win} vezes')
print('FIM ')
