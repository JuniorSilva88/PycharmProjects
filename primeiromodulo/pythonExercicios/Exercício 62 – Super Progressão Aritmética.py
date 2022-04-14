from time import sleep
print('\033[34;1;7mMELHORE O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO, SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS,'
      'O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTAR 0 TERMOS.\033[m ')
primeiro = int(input('Digite o Primeiro termo: '))  # ask termo
razao = int(input('Digite sua Razão: '))  # ask razão
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:  # enquanto não digitar zero, roda o programa abaixo
    total = total + mais
    while contador <= total:
        print('{}  ➡️'.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\n\033[32;1;7mProcessando...\033[m')
sleep(1.75)
print('\nProgressão finalizado com \033[34;1m{}\033[m termos mostrados! '.format(total))
print('Fim! ')
