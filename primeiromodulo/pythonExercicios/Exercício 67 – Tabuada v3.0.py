print('''CRIE UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO DIGITADO FOR NEGATIVO ( CONDIÇÃO DE PARADA)''')
print('-=' * 20)
print('                 \033[1;4mTABUADA\033[m')
while True:
    num = int(input('\033[36;1mDIGITE UM NÚMERO PARA VER SUA TABUADA:\33[m '))
    print('-=' * 20)
    if num < 0:
        break  # condição de parada
    for t in range(1, 11):
        print(f'{num} x {t} = {num*t}')  # utilizando fstrings
print('Fim')
