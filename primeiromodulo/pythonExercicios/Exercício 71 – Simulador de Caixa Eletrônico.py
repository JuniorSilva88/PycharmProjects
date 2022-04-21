print('''CRIE UM PRIGRAMA QUE SIMULE O  FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO PERGUNTAR AO USUÁRIO QUEL SERÁ
O VALOR A SER SACADO (NÚMERO INTEIROS) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES: 
OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$ 50,00 / R$ 20,00 / R$ 10,00 / R$ 1,00 ''')
print('\033[32;1m{:=^40}\033[m'.format('BANCO JR'))
valor = int(input('\033[36;1mQual valor que deseja sacar? R$\033[m '))
print('\033[32;1m{:=^40}\033[m'.format('='))
total = valor
cedula = 200  # maior valor de cédula do Real ( moeda Brasileira R$ )
totalcedula = 0
while True:
    if total >= cedula:  # se o total de cédula for maior ou igual a cédula
        total -= cedula     # tira a maior cédula
        totalcedula += 1  # soma mais uma cédula retirada
    else:
        if totalcedula > 0:
            print(f'\033[36;1mSerão {totalcedula} cédulas de \033[mR$ {cedula:2.2f}')
        if cedula == 200:  # última cédula for a maior
            cedula= 100  # a próxima passa a ser a maior assim sucessivamente
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalcedula = 0
        if total == 0:  # até o valor ser Zero
            break
print('\033[32;1m{:=^40}\033[m'.format('='))
print(f'\033[31;1mValor sacado da conta\033[m R$ {valor:2.2f}')
print('\033[32;1m{:=^40}\033[m'.format('='))
print('Fim')
