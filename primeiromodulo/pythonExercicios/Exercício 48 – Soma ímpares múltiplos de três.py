print('''Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.''')
print(' ')
c
cont = 0  # contator de todos os nº
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1  # total da contagem dos multiplos de 3
        soma += n  # total da soma ddos multiplos de  3
print('A soma de todos \033[44;4;1m{}\033[m é o total de \033[44;4;1m{}.\033[m '.format(cont, soma))
