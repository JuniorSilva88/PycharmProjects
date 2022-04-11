print('''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.''')
num = int(input(' Digite um número para ver sua tabuada:'))
print(' Tabuada do \033[33;1m{}.\033[m'.format(num))
for t in range(1, 11):
    print(' \033[32;1m{}\033[m x \033[34;1m{:2}\033[m = \033[31;1m{}\033[m '.format(num, t, num*t))
