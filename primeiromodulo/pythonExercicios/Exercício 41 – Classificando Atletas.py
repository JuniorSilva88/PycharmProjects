from datetime import date
atual = date.today().year
print('Bem vindo as \033[32;1;4mSELEÇAO BRASILEIRA DE NATAÇÃO\033[m')
print('')
print('''Qual sua sexualidade? \033[31;1m[1] - Feminino:\033[m \33[34;1m[2] - Masculino:\33[m''')
escolha = int(input('Qual sua opção? '))  # escolha da sexualidade em tuplas
nome = str(input('Qual seu nome ? ')).strip()
ano = int(input('Digite qual seu ano de nascimento : '))
idade = atual - ano  # saber qual a idade atual em anos
print('Você nasceu em {}, hoje em {}, você tem {} anos de idade.'.format(ano, atual, idade))
if idade < 9:
    print('{}, Com sua idade de {} anos, você se enquadra na cateogiria \033[31;1;4mMIRIN.\033[m '.format(nome, idade))
elif idade <= 14:
    print('{}, Com sua idade de {} anos, você se engurada na categorai \033[33;1;4mINFANTIL.\033[m '.format(nome, idade))
elif idade <= 19:
    print('{}, Com sua idade de {} anos , você se enqudade da categoria \033[34;1;4mJUNIOR.\033[m '.format(nome, idade))
elif idade <= 25:
    print('{}, Com sua idade de {} anos, você se enquadra na categoria \033[35;1;4mSÊNIOR.\033[m '.format(nome, idade))
else:
    print('{}, Com sua idade de {} anos, você se enquadra na categoria \033[36;1;4mMASTER.\033[m '.format(nome, idade))
print('\033[32;1;4mSeu treinamento começa em 48 horas.\033[m')
