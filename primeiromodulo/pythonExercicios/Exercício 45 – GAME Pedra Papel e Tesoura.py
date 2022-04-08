from random import randint
from time import sleep
print('Crie um programa que faça o computador jogar Jokenpô com você.')
print('{:=^30}'.format(' \033[32;1mJOKEMPÔ\033[m '))
itens = ('Pedra', 'Papel', 'Tesoura')  # lista para escolha
maq = randint(0, 2)  # maq sorteia itens da lista
print('''Opções
[ 0 ] \033[30;4;1mPEDRA\033[m
[ 1 ] \033[31;4;1mPAPEL\033[m
[ 2 ] \033[37;4;1mTESOURA\033[m''')
jogador = int(input('Faça sua escolha: '))
print(' \033[32;1mJO\033[m ')
sleep(1)
print(' \033[32;1mKEN\033[m ')
sleep(1)
print(' \033[32;1mPO\033[m ')
print('\033[36;1m=-\033[m' * 12)
print('Eu escolhi {}! '.format(itens[maq]))
print('Você escolheu {}! '.format(itens[jogador]))
print('\033[36;1m=-\033[m' * 12)
if maq == 0:  # maq jogou PEDRA
    if jogador == 0:
        print('\033[31;1mHÁ NÃO EMPATAMOS.\033[m')
    elif jogador == 1:
        print('\033[34;1mHÁ NÃO EU PERDI.\033[m')
    elif jogador == 2:
        print('\033[33;1mGAME OVER PATINHO.\033[m')
    else:
        print('Jogada inválida')
elif maq == 1:  # maq jogou PAPEL
    if jogador == 0:
        print('\033[33;1mGAME OVER PATINHO.\033[m')
    elif jogador == 1:
        print('\033[31;1mHÁ NÃO EMPATAMOS.\033[m')
    elif jogador == 2:
        print('\033[34;1mHÁ NÃO EU PERDI.\033[m')
    else:
        print('Jogada inválida')
elif maq == 2:  # maq jogou TESOURA
    if jogador == 0:
        print('\033[34;1mHÁ NÃO EU PERDI.\033[m')
    elif jogador == 1:
        print('\033[33;1mGAME OVER PATINHO.\033[m')
    elif jogador == 2:
        print('\033[31;1mHÁ NÃO EMPATAMOS.\033[m')
    else:
        print('Jogada inválida')
