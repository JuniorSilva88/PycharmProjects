from datetime import date  # biblioteca para encontrar o ano atual da maquina

print('''\033[39;1;4mFaça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.\033[m''')
print('')
print('Bem vindo as \033[32;1;4mFORÇAS ARMADAS BRASILEIRA\033[m')
atual = date.today().year  # cód ano atual
print('''Qual sua sexualidade? \033[31;1m[1] - Feminino:\033[m \33[34;1m[2] - Masculino:\33[m''')
escolha = int(input('Qual sua opção? '))  # escolha da sexualidade em tuplas
if escolha == 1:
    print(
        'Para o Sexo Feminino NÃO É OBRIGATÓRIO o Alistamento Militar nas\033[32;1;4mFORÇAS ARMADAS BRASILEIRA\033[m!')
    nf = str(input('Qual seu nome ? ')).strip()
    print('Tenha um bom dia Senhorita {}.'.format(nf))
else:
    print('Para o Sexo Masculino, É OBRIGATÓRIO o Alistamento Militar nas\033[32;1;4mFORÇAS ARMADAS BRASILEIRA\033[m!')
    nm = str(input('Qual seu nome Soldado? ')).strip()
    print('- = ' * 20)
    ano = int(input('\33[34;1m{}\33[m Digite qual seu ano de nascimento : '.format(nm)))
    idade = atual - ano  # saber qual a idade atualizada
    print('\33[34;1m{}\33[m, Você nasceu em {}, hoje em {}, você tem {} anos de idade.'.format(nm, ano, atual, idade))
    if idade == 18:
        print('\033[32;1mCHEGOU SUA VEZ!\033[m Digira-ja se a uma unidade das \033[32;1;4m'
              'FORÇAS ARMADAS BRASILEIRA\033[m e realize seu alistamento.')
    elif idade < 18:
        faltam = (18 - idade)  # quanto tempo falta
        a1 = atual + faltam
        print('Faltam {} anos para seu alistamento, será em \033[31;1m{} NÃO ESQUEÇA!\033[m'.format(faltam, a1))
    else:
        passou = atual - (idade - 18)  # em que ano foi o alistamento
        print('E seu alistamento, foi em \033[36;1m{}\033[m. '.format(passou))
print('- = ' * 20)
