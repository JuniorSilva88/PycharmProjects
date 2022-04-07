print('''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
de acordo com a média atingida:
–Média abaixo de 5.0: \033[31mREPROVADO\033[m
–Média entre 5.0 e 6.9: \033[33mRECUPERAÇÃO\033[m
–Média 7.0 ou superior: \033[32mAPROVADO\033[m''')
n1 = float(input(' Qual foi sua 1ª nota? R: '))
n2 = float(input(' Qual foi sua 2ª nota? R: '))
n3 = float(input(' Qual foi sua 3ª nota? R: '))
n4 = float(input(' Qual foi sua 4ª nota? R: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5.0:
    print(' Sua média foi \033[31;4m{:.2f}\033[m , com isso você está ;\033[31;1mREPROVADO!\033[m '.format(media))
    print(' \033[7;mNOS VEMOS NO ANO PROXIMO ANO LETIVO\033[m')
elif media <= 5.0 or media <= 6.9:
    print(' Sua média foi \033[33;4m{:.2f}\033[m, com isso você está de :\033[33;1mRECUPERAÇÃO!\033[m '.format(media))
    print(' \033[1;mFAÇA A PROVA DE REFORÇO E TIRE A NOTA MÍNIMA, PARA APROVAÇÃO.\033[m')
else:
    media > 7.0
    print(' Sua média foi \033[32;4m{:.2f},\033[m com isso você está :\033[32;1mAPROVADO!\033[m '.format(media))
    print(' \033[4;35mMEUS PARABÉNS!\033[m')

